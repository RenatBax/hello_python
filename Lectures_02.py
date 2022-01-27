# Данные, функции и модули

# Добавление данных в файл - способ 2

# with open('file.txt', 'a') as data:
#     data.write('line 11\n')
#     data.write('line 21\n') # в этом способе ф - close() вызывать не надо

# colors = ['red3', 'green3', 'blue444'] # некоторые данные

# # Добавление данных в файл - способ 1

# #      функ  передали ф некоторые арг
# data = open('file.txt', 'a') # создали файл - арг1, модификатор "а" добавляет некоторые данные в файл - арг2
# # data = open('file.txt', 'w') # старые данные удалятся, а новые запишутся
# # data.writelines(colors) # разделителей в некоторых данных не будет. произвели запись
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close() # закрыли подключение

# exit() # ф - не позволяет читать данные скрипта ниже

# Чтение данных из файла

# path = 'file.txt' # указываем путь к нашему файлу
# data = open(path, 'r') # открываем в режиме чтения 'r'
# for line in data: # пробегаем циклом по строкам в файле
#     print(line)
# data.close()
# # все данные хранятся в текстовом варианте, для работы с числами использовать ф - int
# exit()

# Функции

# Использование функции из другого файла

# import Lectures_01 
# print(Lectures_01.f(1))

# import Lectures_01 as L # назначаем файлу новое название
# print(L.f(1))

# Значения по умолчанию для функций

# def new_string(symbol, count):
#     return symbol * count

# print(new_string('?', 5)) # ?????
# print(new_string('?')) # ошибка
#                    знач по умолч =
# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('?', 5)) # ?????
# print(new_string('?')) # ???
# print(new_string(4)) # 12

# Передача неограниченных аргументов f

# def concatenatio(*params):
#     res: str = "" # явно указываем для перем тип данных, 
#     # res = "" # указывать необязательно
#     # res: int = 0
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))
# print(concatenatio('a', '1', 'd', '2'))
# # print(concatenatio(1, 2, 3, 4))

# Рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

# Кортеж <class 'tuple'> - неизменяемый "список"

# t = ()
# print(type(t)) # <class 'tuple'> - класс кортеж
# t = (1, ) # кортеж из одного элемента
# print(type(t)) 
# t = (1)
# print(type(t)) # <class 'int'>
# t = (28, 9, 1990)
# print(type(t)) # <class 'tuple'>
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# print(type(colors)) # <class 'list'>
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')
# print(type(t)) # <class 'tuple'>
# print(t[0])
# print(t[-2])
# #print(t[20]) # IndexError: tuple index out of range
# for r in t:
#     print(r, end=' ')

# t[0] = 'black' # TypeError: 'tuple' object does not support item assignment
# Ошибка типа: объект "кортеж" не поддерживает назначение элементов

# Распаковка кортежа

# t = tuple(['red', 'green', 'blue']) # создаем список и конвертируем его в кортеж
# red, green, blue = t # распаковываем кортеж в три независимые переменные
# print('r: {} g: {} b: {}' .format(red, green, blue)) # работаем как с отдельными переменными

# a, b = 3, 4 # множественное присваивание
# a = (3, 4, 12, 34)
# # print(a)
# # print(a[0])
# # print(a[-2])
# for item in a:
#     print(item)

# Словари <class 'dict'> (хранилище данных) - неупорядоченные коллекции \
# произвольных объектов с доступом по ключу (число, строка)

# from turtle import down

# dictionary = {}
# dictionary = \
#     {
#         'up': '8',
#         'left': '4',
#         'down': '2',
#         'right': '6'
#     }

# print(dictionary)
# print(type(dictionary)) # <class 'dict'>

# print(dictionary['left'])
# типы ключей могут отличаться

# Ввод нового значения ключа

# print(dictionary['up']) # до
# dictionary['up'] = '89'
# print(dictionary['up']) # после

# Удаление элемента словаря

# print(dictionary)
# del dictionary['down']
# print(dictionary)

# Просмотр содержимого 

# for r in dictionary.keys(): # просмотр всех ключей 'keys'
#     print(r)

# for r in dictionary.values(): # просмотр всех значений 'values'
#     print(r)

# for r in dictionary: # просмотр всех ключей
#     print(r)

# for r in dictionary: # просмотр всех значений
#     print(dictionary[r])

# for item in dictionary:
#     print('{}: {}:'.format(item, dictionary[item]))

# Множества <class 'set'> то же хранилище данных

# colors = {'red', 'green', 'blue'}
# # print(colors)
# # print(type(colors)) # <class 'set'>
# #exit()
# colors.add('red') # одинаковый элемент не добавит
# print(colors)

# colors.add('grey') # добавление элемента
# print(colors)

# # colors.remove('red') # удаление элемента
# # print(colors)
# # colors.remove('red') # удаление несуществующего элемента вызовет ошибку

# colors.discard('red') # тоже удаляет элемент, но при его отсуствии  в множестве не вызывает ошибку
# print(colors)

# colors.clear() # очистка множества
# print(colors)

# Операции с множеством

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# u = a.union(b) # {1, 2, 3, 5, 8, 13, 21} объединение
# i = a.intersection(b) # {8, 2, 5} пересечение
# dl = a.difference(b) #  {1, 3}
# dr = b.difference(a) # {13, 21}
# q = a \
#     .union(b) \
#     .difference(a.intersection(b)) # {1, 21, 3, 13}
# s = frozenset(a) # неизменяемое множество frozenset({1, 2, 3, 5, 8})

# Списки

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# list1[0] = 125
# list2[1] = 333

# for i in list1:
#     print(i, end=' ')
# print()
# for i in list2:
#     print(i, end=' ')

# list3 = [1, 2, 3, 4]

# print(list3, len(list3))

# # print(list3.pop()) # извлекает последний элемент списка
# # print(list3, len(list3))
# # print(list3.pop(2)) # извлекает элемент списка по индексу
# # print(list3, len(list3))

# print(list3.insert(0, 33)) # добавляет  элемент в список по индексу
# print(list3, len(list3))

# print(list3.append(33)) # добавляет  элемент в конец списка
# print(list3, len(list3))