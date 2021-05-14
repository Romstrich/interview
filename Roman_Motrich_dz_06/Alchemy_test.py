from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Vendor(Base):
    __tablename__ = 'vendors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    address = Column(String)

    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def __repr__(self):
        return "<Vendor('%s','%s', '%s')>" %(self.name, self.phone, self.address)


from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///:memory',echo=True)#new_db1.db')#, echo=True)
conn=engine.connect()
result = engine.execute("select * from test_table")
print(result.fetchall())

# vendor = Vendor("ООО ‘Компани’ ", "8(495)77-77-77", "г. Москва, ул. Бажова, д. 9")
# session.add(vendor)

