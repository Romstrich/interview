'''
Усовершенствовать родительский класс таким образом,
чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
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

class ItemDiscountReport(ItemDiscount):
    def __init__(self):
        ItemDiscount.__init__(self)

    def get_parent_data(self):
        print(self.get_name,self.get_coast)

obj=ItemDiscountReport()
obj.get_parent_data()
