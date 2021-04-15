'''
5. Реализовать расчет цены товара со скидкой.
Величина скидки должна передаваться в качестве
аргумента в дочерний класс. Выполнить перегрузку
методов конструктора дочернего класса (метод init,
в который должна передаваться переменная — скидка),
и перегрузку метода str дочернего класса. В этом
методе должна пересчитываться цена и возвращаться
результат — цена товара со скидкой. Чтобы все
работало корректно, не забудьте инициализировать
дочерний и родительский классы (вторая и третья
строка после объявления дочернего класса).
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




obj=ItemDiscountReport(50)
print(obj)

obj.set_parent_data('bread',55)
print(obj)