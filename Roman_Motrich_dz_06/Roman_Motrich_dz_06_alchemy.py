import sqlalchemy

my_engine=sqlalchemy.create_engine('sqlite:///new_db.db',echo=True)
result = my_engine.execute("select * from mygoods")
print(result.fetchall())



