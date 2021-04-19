'''
4. Написать программу, в которой реализовать две функции.
В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим
соответствующее сообщение.
Необходимо открыть файл и подготовить два списка:
с текстовой и числовой информацией. Для создания
списков использовать генераторы. Применить к спискам
функцию zip(). Результат выполнения этой функции
должен должен быть обработан и записан в файл таким
образом, чтобы каждая строка файла содержала текстовое
и числовое значение. Вызвать вторую функцию. В нее
должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие
файла и простой построчный вывод содержимого.
Вся программа должна запускаться по вызову первой
функции.
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
