'''
1. Проверить механизм наследования в Python.
Для этого создать два класса.
    Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре:
название и цену.
    Второй — дочерний (ItemDiscountReport),
должен содержать функцию (get_parent_data), отвечающую
за отображение информации о товаре в одной строке.
Проверить работу программы, создав экземпляр (объект)
родительского класса.
'''


class ItemDiscount:
    def __init__(self):
        self.name = 'any product'
        self.coast = 50

class ItemDiscountReport(ItemDiscount):
    def __init__(self):
        ItemDiscount.__init__(self)


    def get_parent_data(self):
        print(self.name,self.coast)

obj=ItemDiscountReport()
obj.get_parent_data()