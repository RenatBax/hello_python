# Семинар 03 от 27.01.22

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
    # состоящий из элементов последовательности 3k + 1.')

# def d_N(N):
#     dictionary_N = {}
#     for k in range(1, N + 1):
#         res = (3 * k) + 1
#         dictionary_N[k] = res
#     return dictionary_N
    
# print(d_N(5))

print('33. Пользователь задаёт две строки. \
    Определить количество вхождений одной строки в другой.')

# print('34. Подсчитать сумму цифр в вещественном числе.')

# def sum_digits_in_real_number(real_numb = '-234.654'):
#     sum_digits = 0
#     for symbol in real_numb:
#         if not (symbol == '-' or symbol == '.'):
#             sum_digits  += int(symbol)
#     return sum_digits

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

# print('36. Задать список из n чисел последовательности (1+1/n)n и вывести на экран их сумму')

# def sum_of_numbers_in_list(n = 4):
#     numbers_in_list = [(1 + (1 / i) ** i) for i in range(1, n + 1)]
#     print(numbers_in_list) # для наглядности
#     return sum(numbers_in_list)

# print(sum_of_numbers_in_list(10))
exit()

print('37.Задать список из N элементов, заполненных числами из [-N, N]. \
    Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число .')

print('38. Реализовать алгоритм перемешивания списка.')

from random import shuffle, randint
import random
#import random 
a = [2, 8, 4, 3, 1, 5]  
#shuffle(a) 

for i in randint(1, 6):
    a.insert(i )
print(a)

from random import randint
lst = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
count = len(lst) // 2
while count >= 0:
    count1 = randint(0, len(lst)-1)
    temp = lst[count1]
    lst.insert(count1, lst.pop(temp))
    count -= 1
print(lst)


from random import randint
lst = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
count = len(lst)  // 2
while count >= 0:
    count1 = randint(0, len(lst)-1)
    temp = lst[count1]
    lst.pop(count1)
    lst.append(temp)
    count -= 1
print(lst)

exit()
print('39.Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел.')
print('40.Определить, присутствует ли в заданном списке строк, некоторое число.')