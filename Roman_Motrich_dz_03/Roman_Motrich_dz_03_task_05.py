'''
5. Усовершенствовать первую функцию из предыдущего
примера. Необходимо во втором списке часть строковых
значений заменить на значения типа example345
(строка+число). Далее — усовершенствовать вторую
функцию из предыдущего примера (функцию извлечения
данных). Дополнительно реализовать поиск определенных
подстрок в файле по следующим условиям: вывод первого
вхождения, вывод всех вхождений. Реализовать замену
всех найденных подстрок на новое значение и вывод
всех подстрок, состоящих из букв и цифр и имеющих
пробелы только в начале и конце — например, example345.
'''

def write_zip_list(file_name):
    import os.path as path
    import random,string,json
    data_length=15

    if path.isfile(file_name):
        print('Файл существует')
    #else:
    with open(file_name,'w') as f:
        list1 = [i for i in range(data_length)]
        list2 = [random.choice(string.ascii_lowercase) for i in range(data_length)]
        data_pack=zip(list1,list2)
        # json.dump(data_pack, f)
        for i in range(data_length):
            f.write(str(next(data_pack))+'\n')
        f.close()
        read_zip_list(file_name, data_length)


def read_zip_list(file_name,data_length):
    import os.path as path
    import json
    data=None
    if path.isfile(file_name):
        print('Файл существует')
        with open(file_name,'r') as f:
            # data=json.load(f)
            # print(data)
            for i in range(data_length):
                print(f.readline(),end='')
        f.close()


write_zip_list('file_name.txt')
