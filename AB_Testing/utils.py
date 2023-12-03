"""Non-structured functionality"""

import sqlite3

db_path = "ab_testing.sqlite" # hard-coded is bad, change this when you're deploying to prod


class ISQL_Etiquette:
    """Parent class for sql-facing classes"""
    def __init__(self):
        pass


    def chk_conn(conn):
        """Check if connection is still alive"""
        try:
            conn.cursor()
            return True
        except Exception as ex:
            print("CHK_CONN_ERR")
            print(ex)
            return False


    def refresh_conn(self):
        """Make sure the connection is still alive"""
        if not ISQL_Etiquette.chk_conn(self.cnxn):
            self.cnxn = sqlite3.connect(db_path)


    def exec(self, query: str, *args, **kwargs):
        """Executres a given query and commits immediately after"""
        self.refresh_conn()

        cur = self.cnxn.execute(query, *args, **kwargs)
        self.cnxn.commit() 

        return cur
    

    def exec_many(self, query: str, *args, **kwargs):
        """Executres many queries and commits immediately after"""
        self.refresh_conn()

        cur = self.cnxn.executemany(query, *args, **kwargs)
        self.cnxn.commit()

        return cur
