'''
Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет
сгенерирована ошибка выполнения.
'''

class ItemDiscount():
    def __init__(self):
        self.name = 'any product'
        self.coast = 50

    def get_parent_data(self):
        print(self.name,self.coast)

class ItemDiscountReport(ItemDiscount):
    def __init__(self):
        ItemDiscount.__init__(self)


    def get_parent_data(self):
        print(self.name,self.coast)

obj=ItemDiscountReport()
obj.get_parent_data()