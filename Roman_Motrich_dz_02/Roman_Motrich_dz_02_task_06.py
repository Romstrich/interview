'''
6. Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport
на два класса. Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info, которая в
первом классе будет отвечать за вывод названия товара,
а вторая — его цены. Далее реализовать выполнение
каждой из функции тремя способами.
'''

class ItemDiscount():
    def __init__(self):
        self.__name = 'any product'
        self.__coast = 50

    @property
    def get_name(self):
        return self.__name

    @property
    def get_coast(self):
        return self.__coast

    def set_name(self,new_name):
        self.__name=new_name

    def set_coast(self,new_coast):
        self.__coast=new_coast

class ItemDiscountReport(ItemDiscount):
    def __init__(self,sale=0):
        ItemDiscount.__init__(self)
        self._sale=sale
        #self.set_coast(int(self.get_coast*(1-(self._sale/100))))

    def get_parent_data(self):
        return f'name:{self.get_name}, coast:{self.get_coast}'

    def set_parent_data(self,name,coast):
        self.set_name(name)
        self.set_coast(coast)

    def __str__(self):
        if self._sale!=None:
            return f'name:{self.get_name}, coast:{self.get_coast*(1-(self._sale/100))}'
        else:
            return self.get_parent_data()

class product_1(ItemDiscountReport):
    def __init__(self):
        ItemDiscountReport.__init__(self)

    def get_info(self):
        print(self.get_name)

class product_2(ItemDiscountReport):
    def get_info(self):
        print(self.get_coast)



obj=ItemDiscountReport(50)
print(obj)

obj.set_parent_data('bread',55)
print(obj)

a=product_1()
b=product_2()
a.get_info()
b.get_info()