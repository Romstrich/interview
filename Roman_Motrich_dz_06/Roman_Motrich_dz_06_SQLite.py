import sqlite3

# my_db='new_db.db'
# my_connect=sqlite3.connect(my_db)
# my_cursor=my_connect.cursor()
# print(my_cursor.execute('SELECT * FROM mygoods').fetchall(),end='\n\n')
# print(my_cursor.execute('SELECT * FROM table_01').fetchall(),end='\n\n')
#
# my_connect.commit()
# my_connect.close()

class MyDataBase():
    def __init__(self,db_path):
        self.connect=sqlite3.connect(db_path)
        self.cursor=self.connect.cursor()
        self.Goods=goods()

    class goods:
        def __init__(self):
            MyDataBase.cursor.execute('create table if not exists projects(id integer, name text)')
        pass

    class units:
        pass

    class positions:
        pass

    class employers:
        pass

    class vendors:
        pass

    def close(self):
        self.connect.close()


m_base=MyDataBase('new_db.db')