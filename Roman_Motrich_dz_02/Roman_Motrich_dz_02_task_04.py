'''
4. Реализовать возможность переустановки значения
цены товара. Необходимо, чтобы и родительский, и
дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий
метод родительского класса и функцию дочернего
(функция, отвечающая за отображение информации
о товаре в одной строке).
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
    def __init__(self):
        ItemDiscount.__init__(self)

    def get_parent_data(self):
        print(self.get_name,self.get_coast)

    def set_parent_data(self,name,coast):
        self.set_name(name)
        self.set_coast(coast)



obj=ItemDiscountReport()
obj.get_parent_data()

obj.set_parent_data('bread',55)
obj.get_parent_data()