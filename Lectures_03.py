# Лекция 3 01.02.2022

# Анонимные методы. Лямбда
# def f(x):
#     x ** 2

# g = f
# print(f(1))
# print(g(1))

# def f(x):
#     return x ** 2

# g = f
# print(type(f))
# print(type(g))
# print(f(3))
# print(g(4))

# def calc1(x):
#     return x + 10

# print(calc1(10))

# def calc2(x):
#     return x * 10

# print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)

# def sum(x, y):
#     return x + y

# f = sum
# f = lambda q, r: q + r # для примера не работ
# f = lambda x, y: x + y # работ
# sum = lambda x, y: x + y + 4 # переписанная функ sum работ

# def mylt(x, y):
#     return x * y

# def calc(op, a, b):
#     print(op (a, b))

# calc(mylt, 4, 5)
# calc(f, 5, 5)
# calc(sum, 5, 5)

# calc(lambda x, y: x + y, 5, 7)

# List Comprehension - для быстрого создания списков

# [exp <if conditional> for item in iterable (if conditional)]

# list = []
# for i in range(1, 10):
#     # if i%2 == 0:
#         list.append(i)
# print(list)
 
# выраж     
# # [exp for item in iterable]
# list = [i for i in range(1, 21)]
# print(list)

# # выборка по условию
# # [exp for item in iterable (if conditional)]
# list = [i for i in range(1, 21) if i%2 == 0]
# print(list)

# # подключаем кортеж
# list = [(i, i) for i in range(1, 21) if i%2 == 0]
# print(list)

# def f(x):
#     return x ** 3
# # подключаем функцию   
# list = [f(i) for i in range(1, 21) if i%2 == 0]
# print(list)

# list2 = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
# print(list2)

### Задача по выборке из файла четных чисел возведение их в куб \
# и показ в виде кортежа(число, число в кубе)
# path = # ссылка на файл на жд
# f = open(path, 'r') # открываем файл для редактирования
# data = f.read() + ' ' # считываем и добавляем пробел между данными в файле
# f.close закрываем файл

# numbers = [] # создаем пустой лист

# while data != '': # пробегаясь по строке файла data которую считали на 93 строке пока она не пустая
#     space_pos = data.index(' ') # находим первую позицию пробела 
#     numbers.append(int(data[:space_pos])) # взять что находится от первого символа до пробела и добавить в лист преобразовывая в число
#     data = data[:space_pos + 1:] # обновляем строку с учетом того что добавили в выборку 

# out = [] # создаем еще один пустой лист уже для решения

# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)

# def select(f, coll): # принимает функ и набор данных
#     return [f(x) for x in coll] # возвр список

# def where(f, coll): # # принимает функ и набор данных
#     return [x for x in coll if f(x)] # возвр список

# data = '1 2 3 5 8 15 23 38'.split() # берем готовую строку не считывая, на выходе набор строк
# #   Ф  преобр стр в число, набор данных из файла и вовр новый лист
# res = select(int, data) # 
# #     Ф лямбда провер числа на четность, из данных стр 118 и возвр обновл лист
# res = where(lambda x: not x % 2, res) 
# # Ф лямбда возводит числа в квадрат и преобр в кортеж, из данных стр 120 и возвр лист
# res = select(lambda x: (x, x ** 2), res) #
# print(res)

# with open(f, r) as F: Решение задачи
#    l = [int(i) for x in F]
#    m = [(i, lambda i: i ** 3) for i in l if i % 2 == 0] 

# Функция map() - применяет указанную функцию к каждому элементу итерируемого объекта \
# и возвр итератор с новыми объектами
# f(x) => x + 10
# map(f, [1, 2, 3]) => [11, 12, 13] нельзя пройтись дважды!!!!

# li = [x for x in range(1, 20)]         
# li = list(map(lambda x: x + 10, li))
# print(li)

# data = input() # ввод с клавиатуры
# data = input().split() # ввод с клавиатуры и разделяем числа по умолчанию пробел, можно ???(',')
# в map в качестве аргумента Ф int, преобраз введ с клав числа из стр в числа
# data = map(int, input().split()) # без преобраз в лист данные можно получить так
# data = map(int, '1 33 4 7'.split())
# # data = list(map(int, '1 33 4 7'.split())) # без преобраз в лист переработанный данные  функ map не сохраняюся
# for i in data:
#     print(i * 2, end=' ')
# print('--') 
# for i in data:
#     print(i * 2, end=' ')
# data = list(map(int,input().split())) #
# print(data)

# def where(f, coll): 
#     return [x for x in coll if f(x)]

# data = '1 2 3 5 8 15 23 38'.split() 
# res = map(int, data)
# res = where(lambda x: not x % 2, res) 
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# Функция filter - применяет указанную функцию к каждому элементу итерируемого объекта \
# и возвр итератор с теми объектами, для которых функция вернула True
# (x) => x - четное
# filter(f, [1, 2, 3, 4]) => [   2,   4] нельзя пройтись дважды!!!!

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data))
# print(res)

# data = '1 2 3 5 8 15 23 38'.split() 
# res = map(int, data)
# res = filter(lambda x: not x % 2, res) 
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# Функция zip - применяется к набору итерируемых объектов \
# и возвращает итератор с кортежами из элементов входных данных
# Кол-во элементов в рез-те равно мин колич элементов входного набора
# zip ([1, 2, 3], ['о', 'а', 'ч'], ['j', 'h', 'n'])
#     [(1, 'о', 'j'), (2, 'а', 'h'), (3, 'ч', 'n')] нельзя пройтись дважды!!!!

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids))
# print(data)
# data2 = list(zip(users, ids, salary))
# print(data2)

# # Функция enumerate - применяется к итерируему объекту и возвращает \
# # новый итератор с кортежами из индексов и элементов входных данных
# # нельзя пройтись дважды!!!!

# data = list(enumerate(salary))
# print(data)