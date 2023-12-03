# Adding non structured functionality


class ISQL_Etiquette:
    """Parent class for sql-facing classes"""
    def __init__(self):
        pass
    
    def exec(self, query: str, *args, **kwargs):
        """Executres a given query and commits immediately after"""
        cur = self.cnxn.execute(query, *args, **kwargs)
        self.cnxn.commit()

        return cur
    

    def exec_many(self, query: str, *args, **kwargs):
        """Executres many queries and commits immediately after"""
        cur = self.cnxn.executemany(query, *args, **kwargs)
        self.cnxn.commit()

        return cur
