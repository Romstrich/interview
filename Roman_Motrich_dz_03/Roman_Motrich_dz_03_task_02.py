'''
2. Написать программу, которая запрашивает
у пользователя ввод числа. На введенное число
она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить
сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать
значение True, иначе False.
'''


import re
with_comma=re.compile(r'^[0-9]*,[0-9]*$',re.S)
without_comma=re.compile(r'^[0-9]*$',re.S)

def comma_splitter():

    nomber=input('Введите число ')
    if with_comma.search(nomber):
        print('Дробное число')
        if nomber.split(',')[0] == nomber.split(',')[1]:
            return True
        else:
            return False
    elif without_comma.search(nomber):
        print('Целое число ')
    else:
        pass


print(comma_splitter())