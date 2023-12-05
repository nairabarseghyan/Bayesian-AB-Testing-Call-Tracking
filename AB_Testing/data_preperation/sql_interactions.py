"""Classes to handle sql interactons"""

import sqlite3
import logging
import pandas as pd
import numpy as np
import os
from ..logger import CustomFormatter
from ..data_preperation.schema import create_ORM
from ..utils import ISQL_Etiquette, db_path

logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

class SqlHandler(ISQL_Etiquette):
    """Handles all interactions with the database"""

    def __init__(self, table_name: str) -> None:
        super().__init__()
        
        self.cnxn = sqlite3.connect(db_path)
        self.table_name = table_name

        cur = self.exec(f'SELECT l.name FROM pragma_table_info("{table_name}") as l WHERE l.pk = 1;')
        self.pk = list(cur)[0][0]


    def __enter__(self):
        """Interfaces python `with` syntax"""
        return self


    def __exit__(self, *args, **kwargs):
        """Exits the python `with` scope"""

        self.close_cnxn()


    def close_cnxn(self)->None:
        """Close the connection gracefully"""

        logger.info('commiting the changes')
        self.cnxn.commit()
        logger.debug('closing connection')
        self.cnxn.close()
        logger.info('the connection has been closed')


    def insert_one(self, **kwargs) -> None:
        """Insert a single row into the table"""

        query = f"INSERT INTO {self.table_name} ({', '.join([k for k in kwargs.keys()])}) VALUES ({', '.join(['?'] * len(kwargs))});"
        logging.debug(query, [v for v in kwargs.values()])

        cur = self.exec(query, [v for v in kwargs.values()])
        logging.info("insert_one: " + str(list(cur)))


    def get_table_columns(self) -> list:
        """Gets a list of the column names that belong to the table"""

        cur = self.exec(f"PRAGMA table_info({self.table_name});")
        columns = cur.fetchall()

        column_names = [col[1] for col in columns]
        logger.info(f'the list of columns: {column_names}')

        return column_names


    def truncate_table(self) -> None:
        """Deletes all rows of the table"""

        query=f"delete from {self.table_name} where 1=1;"
        logging.info(f'the {self.table_name} is being truncated')
        self.exec(query)


    def drop_table(self):
        """Drops the table from the database"""

        query = f"DROP TABLE IF EXISTS {self.table_name};"
        logging.info(query)

        self.exec(query)
        logging.info(f"table '{self.table_name}' deleted.")


    def insert_many(self, df: pd.DataFrame) -> str:
        """Insert many values at once into the table"""

        df = df.replace(np.nan, None)
        df.rename(columns = lambda x: x.lower(), inplace=True)
        
        columns = list(df.columns)
        logger.info(f'BEFORE the column intersection: {columns}')

        sql_column_names = [i.lower() for i in self.get_table_columns()]
        columns = list(set(columns) & set(sql_column_names))
        logger.info(f'AFTER the column intersection: {columns}')

        assert len(df.columns) == len(sql_column_names), "Mismatch in columns between the dataframe and the sql table. \ndf.columns: " + \
            ", ".join(df.columns) + "\nsql columns: " + ", ".join(sql_column_names)
        
        ncolumns = list(len(columns) * '?')
        data_to_insert = df.loc[:, columns]
        values = [tuple(i) for i in data_to_insert.values]

        logger.info(f'the shape of the table which is going to be imported {data_to_insert.shape}')

        if len(columns)>1:
            cols, params =', '.join(columns), ', '.join(ncolumns)
        else:
            cols, params = columns, ncolumns

        logger.info(f'insert structure: colnames: {cols} params: {params}')
        logger.info(values[0])
        query=f"""INSERT INTO {self.table_name} ({cols}) VALUES ({params});"""

        logger.info(f'QUERY: {query}')

        cur = self.exec_many(query, values)

        try:
            for i in cur.messages:
                logger.info(i)
        except:
            pass

        logger.warning('the data is loaded')


    def from_sql_to_pandas(self, chunksize:int=64) -> pd.DataFrame:
        """
        Converts the table into a pandas dataframe and returns it, 
        reads the table in `chnksize`-sized chunks
        """

        offset=0
        dfs=[]

        while True:
            query=f"""
            SELECT * FROM {self.table_name}
                LIMIT {chunksize}  
                OFFSET {offset}
            """
            data = pd.read_sql_query(query, self.cnxn)
            self.cnxn.commit()

            logger.info(f'the shape of the chunk: {data.shape}')

            dfs.append(data)
            offset += chunksize
            
            if len(dfs[-1]) < chunksize:
                logger.info('loading the data from SQL is finished')
                logger.debug('connection is closed')
                break

        df = pd.concat(dfs)

        return df


    def update_table(self, set_values: dict, condition: str):
        """Updates some the values of some fields of some rows (based on the condition)"""

        if not set_values:
            logger.warning('No values to update. Provide set_values.')
            return

        set_clause = ', '.join(f"{col} = ?" for col in set_values.keys())
        values = list(set_values.values())

        query = f"""
        UPDATE {self.table_name}
        SET {set_clause}
        WHERE {condition};
        """

        cur = self.exec(query, values if hasattr(values, "__iter__") else list(values))
        
        logger.info(f"Rows updated: {cur.rowcount}")


    def update_one(self, id: int, **kwargs: dict):
        """Updates a single row in the table"""

        cond = self.pk + " = " + str(id)
        self.update_table(kwargs, cond)


    def select_one(self, id: int, cols: list = []) -> dict:
        """Selects only one row and returns it as a python dictionary"""

        cond = self.pk + " = ?"
        query = f"select {'*' if len(cols) == 0 else ', '.join(cols)} from {self.table_name} where {cond}"
        cur = self.exec(query, (id, ))
        
        return {k:v for k, v in zip(self.get_table_columns() if len(cols) == 0 else cols, list(cur)[0])}
    

    def get_next_id(self):
        """Conveniently gets the increment of the previous id (used for creating a new entry)"""
        
        query = f"select (max({self.pk}) + 1) from {self.table_name};"
        cur = list(self.exec(query))
        cur = cur[0]
        
        return 0 if cur is None else cur[0] if cur[0] is not None else 0
