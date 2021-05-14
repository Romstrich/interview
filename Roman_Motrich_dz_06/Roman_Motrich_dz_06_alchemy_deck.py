# import sqlalchemy

# my_engine=sqlalchemy.create_engine('sqlite:///new_db.db')
# result = my_engine.execute("select * from mygoods")
# print(result.fetchall())
from sqlalchemy import text, ForeignKey
# import units as units
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import mapper

Base = declarative_base()


class Positions(Base):
    __tablename__ = 'positions'
    position = Column(String, primary_key=True)

    def __init__(self, position):
        self.position = position

    def __repr__(self):
        return f"<Positions('{self.position}')>"


class Units(Base):
    __tablename__ = 'units'
    #unit = Column(String, primary_key=True)
    unit = Column(String, ForeignKey("unit"), primary_key=True)

    def __init__(self, unit):
        self.unit = unit

    def __repr__(self):
        return f"<Units('{self.unit}')>"


class Employees(Base):
    __tablename__ = 'employees'
    employe_id = Column(Integer, primary_key=True)
    employe_fio = Column(String)

    def __init__(self, employe_fio):
        self.employe_fio = employe_fio

    def __repr__(self):
        return f"<Employees('{self.employe_fio}')>"


class Vendors(Base):
    __tablename__ = 'vendors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ownerchipform = Column(String)
    address = Column(String)
    phone = Column(String)
    email = Column(String)

    def __init__(self, name, phone, address, ownerchipform, email):
        self.name = name
        self.phone = phone
        self.address = address
        self.ownerchipform = ownerchipform
        self.email = email

    def __repr__(self):
        return f"<Vendor('{self.name}','{self.phone}', '{self.address}','{self.ownerchipform}','{self.email}')>"  # %(self.name, self.phone, self.address)


class Categories(Base):
    __tablename__ = 'categories'
    category_name = Column(String, primary_key=True)
    category_description = Column(String)

    def __init__(self, category_name, category_description):
        self.category_name = category_name
        self.category_description = category_description

    def __repr__(self):
        return f"<Categories('{self.category_name}','{self.category_description}')>"


class Goods(Base):
    __tablename__ = 'goods'
    good_id = Column(Integer, primary_key=True)
    good_name = Column(String)
    good_unit = Column(String)
    good_unit = Column(String, ForeignKey('unit.id'))  # Проба связи с таблицей Units
    #good_unit = relationship("Units", backref='unit')
    good_cat = Column(String)

    def __init__(self, good_name, good_unit, good_cat):
        self.good_name = good_name
        self.good_unit = good_unit
        self.good_cat = good_cat

    def __repr__(self):
        return f"<Goods('{self.good_name}','{self.good_unit}','{self.good_cat}')"


# Подключение
engine = create_engine('sqlite:///m_db.sqlite3', echo=True)
Base.metadata.create_all(engine)
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
# Тестовый ввод данных
vendor = Vendors("ООО ‘Компани’ ", "8(495)77-77-77", "г. Москва, ул. Бажова, д. 9", "ОАО", "vendor@mail.ru")
position = Positions('Моя позиция1')
employe = Employees('Петрович')
good = Goods('Товар', 'шт', 'книга')
unit = Units('шт')
try:
    session.add(vendor)
    session.add(good)
    session.add(employe)
    #session.add(unit)
    #session.add(position)

    session.commit()
except BaseException as e:
    print(e)
# Закрытие сессии
session.close()
engine.dispose()
