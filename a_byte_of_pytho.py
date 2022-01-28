# Переменное число параметров
# def total(initial=5, *numbers, **keywords):
#     count = initial
#     for number in numbers:
#         count += number
#     for key in keywords:
#         count += keywords[key]
#     return count

# print(total(10, 1, 2, 3, vegetables=50, fruits=100))

# Ключевые параметры
# Объявление параметров после параметра со звёздочкой даёт только ключевые аргументы

# def total(initial=5, *numbers, extra_number): #  def total(initial=5, *, extra_number).
#     count = initial
#     for number in numbers:
#         count += number
#     count += extra_number
#     print(count)

# total(10, 1, 2, 3, extra_number=50)
# # total(10, 1, 2, 3) # Вызовет ошибку, поскольку мы не указали значение
# # аргумента по умолчанию для 'extra_number'.

# def someFunction():
#     pass
# print(someFunction())

# def printMax(x, y):
#     '''Выводит максимальное из двух чисел. 
        
#         Оба значения должны быть целыми числами.''' 
#         # строка документации для этой функции
#     x = int(x) # конвертируем в целые, если возможно
#     y = int(y)
#     if x > y:
#         print(x, 'наибольшее')
#     else:
#         print(y, 'наибольшее')
# printMax(3, 5)
# print(printMax.__doc__)

from itertools import count
from random import randint


# list = [1, 3, 4, 5]
# j = 0
# for i in list:
#     print(f'{i} - {j}')
#     j += 1
# for j in list:
#     print(f'list{[j]}')
# for i in range(len(list)):
#     print(f'{i}')  


# from random import randint
# list = []

# size = 12
# count = 0
# while count < size:
#     i = randint(-9, 10)
#     list.append(i)
#     count += 1
# print(list)

# def create_list(len = 10, min = 1, max = 50):
#     return [randint(min, max) for i in range(len)]

# def create_two_dimensional_list(\
#     raw = 3, col = 4, min = 1, max = 50):

#     return [[randint(min, max) for i in range(col)]\
#         for j in range(raw)]

# print(create_list())

# print(create_two_dimensional_list())

def get_cubes(namber = 6):
    return [((-3) ** i) for i in range(namber)]

print(get_cubes())