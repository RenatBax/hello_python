# Семинар 03 от 27.01.22

from cmath import sqrt
from dataclasses import replace
from itertools import count
from math import *
from modulefinder import ModuleFinder
from random import random, shuffle, randint
import string

new_text = 'При первом вызове, func (3, 7), параметр a получает значение 9, параметр b \
получает значение 11, а c получает своё значение по умолчанию, равное 10. \
При втором вызове func (25, c=24) переменная a получает значение 26 в силу \
позиции аргумента. После этого параметр c получает значение 23 по имени, \
т.е. как ключевой параметр. Переменная b получает значение по умолчанию, \
равное 5.'

# print('31. Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.')

# def create_list(N = 12): 
#     list_N = [] 
#     res = 1
#     for i in range(0, N + 1):
#         if len(list_N) % 2:
#             res = -3 ** i
#             list_N.append(res)
#         else: 
#             res = 3 ** i
#             list_N.append(res)
#     return list_N

# print(create_list())

# print('32. Для натурального N создать словарь индекс-значение, \
#     состоящий из элементов последовательности 3k + 1.')

# def d_N(N):
#     dictionary_2 = {k: (3 * k) + 1 for k in range(1, N + 1)}
#     dictionary_N = {}
#     for k in range(1, N + 1):
#         res = (3 * k) + 1
#         dictionary_N[k] = res
#     return dictionary_N, dictionary_2
    
# print(d_N(5))

# print('33. Пользователь задаёт две строки. \
#     Определить количество вхождений одной строки в другой.')

# def the_number_of_occurrences_of_one_string_in_another(s_1, s_2):
#     count = 0
#     u = 0
#     while u < len(s_2):
#         for i in s_1:
#             for j in s_2:
#                 if i == j:
#                     count += 1           
#         u += 1
#     return (count // u) // u

# string_1 = input('Введите любое предложение: ')
# string_2 = input('Введите еще раз любое предложение: ')
# print(the_number_of_occurrences_of_one_string_in_another\
#     (string_1, string_2))

# #     return s_1.count(s_2) решение с помощью библиотеки

# # def the_number_of_occurrences_of_one_string_in_another_2(s_1, s_2):
# # # решение Рустема Абубакарова
# #     i = 0
# #     count = 0
# #     while i < len(s_1):
# #         j = 0
# #         if s_1[i] == s_2[0]:
# #             while j < len(s_2):
# #                 if j + i >= len(s_1) - 1:
# #                     if j == len(s_2) - 1:
# #                         count += 1
# #                         break
# #                     else: 
# #                         break
# #                 elif s_1[i + j] != s_2[j]: 
# #                     break
# #                 elif j == len(s_2) - 1: 
# #                     count += 1 
# #                 j += 1  
# #         i += 1 
# #     return count

# # print(the_number_of_occurrences_of_one_string_in_another_2\
# #     (string_1, string_2))

# print('34. Подсчитать сумму цифр в вещественном числе.')

# def sum_digits_in_real_number(real_numb = '-123.123'):
#     real_numb = real_numb\
#         .replace('-', '')\
#         .replace('+', '')\
#         .replace('.', '')
#     return sum(int(i) for i in real_numb)

# print(sum_digits_in_real_number())  

# print('35. Написать программу получающую набор произведений чисел от 1 до N.\
#     Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ].')

# def product_number_of_segment(number = 6):
#     list_numbers = []
#     product = 1
#     for i in range(1, number):
#         product *= i
#         list_numbers.append(product)
#     return list_numbers

# print(product_number_of_segment(10))

# print('36. Задать список из n чисел последовательности \
#       (1+1/n)n и вывести на экран их сумму')

# def sum_of_numbers_in_list(n = 4):
#     numbers_in_list = [(1 + (1 / i) ** i) for i in range(1, n + 1)]
#     print(numbers_in_list) # для наглядности
#     return sum(numbers_in_list)

# print(sum_of_numbers_in_list(10))

# print('37.Задать список из N элементов, заполненных числами из [-N, N]. \
#       Найти произведение элементов на указанных позициях. \
#       Позиции хранятся в файле file.txt в одной строке одно число .')

# # Задать список из N элементов, заполненных числами из [-N, N]
# def create_list_number(N = 10): 
#     return [randint(-N, N) for i in range(N)]
# # Позиции хранятся в файле file.txt в одной строке одно число 
# def create_text_file(list_N, name_file = 'task_37.txt', mode = 'w'):
#     with open(name_file, mode) as data:
#         for i in range(0, len(list_N)):
#             data.write(f'{i}\n') # аргумент write() должен быть str, а не list
#     return name_file
# # Найти произведение элементов на указанных позициях
# def prodact_number_in_list(lst, rd = ''):
#     with open(rd, 'r') as fl:
#         list_N_idx = [int(line)for line in fl]
#     product = 1
#     for i in range(0, len(list_N_idx)):
#         temp = lst[i]
#         if temp != 0:
#             product *= temp 
#         #print(f'{i} - {temp}')
#     return product 

# list_number = create_list_number()
# print(list_number)
# new_file = create_text_file(list_number)
# print(prodact_number_in_list(list_number, new_file))

# print('38. Реализовать алгоритм перемешивания списка.')

# lst = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
# # Штатный
# lst = [2, 8, 4, 3, 1, 5]  
# shuffle(lst) 
# print(lst)

# # Рабочий
# def shuffling_the_list(mixed):
#     count = len(mixed) # // 2
#     while count >= 0:
#         count1 = randint(0, len(mixed)-1)
#         temp = mixed[count1]
#         mixed.pop(count1)
#         mixed.append(temp)
#         count -= 1
#     return mixed
    
# print(shuffling_the_list(lst))

# # Хромающий
# count = len(lst) // 2
# while count >= 0:
#     count1 = randint(0, len(lst)-1)
#     temp = lst[count1]
#     lst.insert(count1, lst.pop(temp))
#     count -= 1
# print(lst)

# print('39.Реализовать алгоритм задания случайных чисел. \
#       Без использования встроенного генератора псевдослучайных чисел.')

# def random_number(r_start, r_end):
#     '''Линейный конгуэнтный метод предложен Д.Г. Лехмером в 1949 г.
        
#         В основе лежит набор из четырех ключевых чисел
#         m > 0, модуль;
#         0 <= a <= m, множитель;
#         0 <= c < = m, приращение;
#         0 <= Xo <= m, начальное значение.
#         Последовательность получается по формуле:
#             Xn+1 = (a*Xn + c) mod m, n >= 1
#         Ключ Xo. В данной формуле крайне выжен выбор параметров.'''
#     modul = r_end
#     #increment = modul // 2
#     multiplier = r_start * 2
#     list_rnd = []
#     for i in range(r_end):
#         r_start = (multiplier * r_start + i) % modul
#         list_rnd.append(r_start)
#     return list_rnd

# print(random_number(1, 20))
# print(random_number.__doc__)

# print('40.Определить, присутствует ли в заданном списке строк, некоторое число.')

# def find_some_number(Text, find_number):
#     # for symbol in Text:
#     #     if symbol != find_number:
#     #         continue 
#     #     else:
#     #         return 'The specified number is present'           
#     # return 'The specified number is nor present'

#     if find_number in Text:
#         return True
#     else: return False

# n = input('Enter number: ')
# print(find_some_number(new_text, n))
