"""Non-structured functionality"""

import sqlite3
from .config import db_path



class ISQL_Etiquette:
    """Parent class for sql-facing classes"""
    def __init__(self):
        pass


    def chk_conn(conn):
        """Check if connection is still alive

        Args:
            conn (sqlite3.connection): connection

        Returns:
            bool: True if is alive, false otherwise
        """        
        
        try:
            conn.cursor()
            return True
        except Exception as ex:
            return False


    def refresh_conn(self):
        """Make sure the connection is still alive"""
        if not ISQL_Etiquette.chk_conn(self.cnxn):
            self.cnxn = sqlite3.connect(db_path)


    def exec(self, query: str, *args, **kwargs):
        """Executres a given query and commits immediately after

        Args:
            query (str): query string

        Returns:
            sqlite3.Cursor: cursor
        """       
        self.refresh_conn()

        cur = self.cnxn.execute(query, *args, **kwargs)
        self.cnxn.commit() 

        return cur
    

    def exec_many(self, query: str, *args, **kwargs):
        """Executres many queries and commits immediately after

        Args:
            query (str): query string

        Returns:
            sqlite3.Cursor: cursor
        """        

        self.refresh_conn()

        cur = self.cnxn.executemany(query, *args, **kwargs)
        self.cnxn.commit()

        return cur
