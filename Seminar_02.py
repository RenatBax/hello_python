# Семинар 02 от 24.01.22

# print('17. По двум заданным числам проверять является ли одно квадратом другого.') 

# def square_of_other(number_1, number_2):
#     if number_1 // number_2 == number_2:
#         print(number_2, 'square', number_1)
#     elif number_2 // number_1 == number_1:
#         print(number_1, 'square', number_2)
#     else:
#         print('Are not squares')

# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
# square_of_other(a, b)

# print('18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y.') 

# def true_or_false(x, y):
#     # if not (x or y) == (not x and not y): 
#     #     print(True)
#     # else: 
#     #     print(False)
#     print(not (x or y) == (not x and not y))

# true_or_false(x = int(input('Enter x: ')), y = int(input('Enter y: ')))

# def true_or_false_2():
#     for x in range(2):
#         for y in range(2):
#             print(x, y, (not (x or y) == (not x and not y)))

# true_or_false_2()

# def true_or_false_3():
#     X = [0, 1]
#     Y = [1, 0]
#     for x in X:
#         for y in Y:
#             print(x, y, (not (x or y) == (not x and not y)))

# true_or_false_3()

# def true_or_false_4(x, y):
#     return (not (x or y) == (not x and not y))

# print(true_or_false_4(True, False))
# print(true_or_false_4(True, True))
# print(true_or_false_4(False, True))
# print(true_or_false_4(False, False))


# print('19. Определить номер четверти плоскости, в которой находится точка\
#  с координатами Х и У, причем X ≠ 0 и Y ≠ 0.')

# def determine_the_quarter_number(x, y):
#     if x > 0 and y > 0: return 1
#     elif x < 0 and y > 0: return 2
#     elif x < 0 and y < 0: return 3
#     else: return 4

# q = int(input('Введите координату Х: '))
# w = int(input('Введите координату Y: '))
# quarter_number = determine_the_quarter_number(q, w) 
# print('Номер четверти плоскости:', quarter_number)   

# print('20. Задать номер четверти, показать диапазоны для возможных координат.')

# def set_the_quarter_number(quarter_number):
#     if quarter_number == 1: print('Диапазон возможных координат: x > 0; y > 0')
#     elif quarter_number == 2: print('Диапазон возможных координат: x < 0; y > 0')
#     elif quarter_number == 3: print('Диапазон возможных координат: x < 0; y < 0')
#     elif quarter_number == 4: print('Диапазон возможных координат: x > 0; y < 0')
#     else: print('Такой четверти не существует.')

# set_the_quarter_number(quarter_number = int(input('Задайте номер четверти: ')))

# print('21. Программа проверяет пятизначное число на палиндромом.')

# def palindrome(number): 
    
#     if number[0] == number[4] and number[1] == number[3]:
#         print('Введенное число - палиндром.')
#     else:
#         print('Введенное число - не палиндром.')

# u = input('Введите пятизначное число: ')
# palindrome(u)

# print('22. Найти расстояние между точками в пространстве 2D/3D.')

# import math
# from xmlrpc.client import MultiCallIterator

# def distance_between_points(a1, a2, b1, b2, z1, z2):
#     from math import sqrt
#     print('distance_2D =', round(sqrt(pow(a2 - a1, 2) + pow(b2 - b1, 2)), 4))
#     print('distance_3D =', round(sqrt(pow(a2 - a1, 2) + pow(b2 - b1, 2) + pow(z2 - z1, 2)), 5))

# distance_between_points(1, 3, -6, 9, 0, -7)

# print('23. Показать таблицу квадратов чисел от 1 до N.')

# def table_of_squares_of_numbers(number_N):
#     for i in range(1, number_N + 1):
#         print(i, '--', round(math.pow(i, 2)))

# N = int(input('Введите число N, для создания диапазона чисел: '))
# table_of_squares_of_numbers(N)

# print('24. Найти кубы чисел от 1 до N.')

# def cubes_of_numbers(N):
#     cub = []
#     for i in range(1, N + 1):
#         print(i)
#         cub.append(pow(i, 3))
#     print('Кубы чисел: ', cub)

# number_N = int(input('Введите число N: '))
# cubes_of_numbers(number_N)

# print('25. Найти сумму чисел от 1 до А.')

# def sum_of_numbers(number_A):
#     sum = 0
#     for i in range(1, number_A + 1):
#         sum += i
#         print(i ,  end='+')
#     print(' =',  sum)

# sum_of_numbers(20)

# print('26. Возведите число А в натуральную степень B используя цикл.')

# def raise_a_number_to_a_power(number_A, power):
#     multi = 1
#     count = 0
#     while count < power:
#         multi *= number_A
#         count += 1
#         print(f'{number_A} ^ {count} = {multi}')
    
#     result = 1
#     for i in range(1, power + 1): # c циклом for 
#         result *= number_A
#         print(f'{number_A} ^ {i} = {result}')

# raise_a_number_to_a_power(5, 4)

# print('27 Определить количество цифр в числе.')

# def number_of_digits(number): 
#     for i in number:
#         if i == '.' or i == '-':
#             return len(number) - 1
#         elif i == '-' and i == '.':
#             return len(number) - 2
#         else:
#             return len(number)

# h = input('Введите число: ')
# d = number_of_digits(h)
# print(f'Количество цифр в числе: {d}.')

# def number_of_digits_2(number_M): # математ способ
#     count = 0
#     while number_M != 0 and number_M != -1:
#         number_M //= 10
#         count += 1
#     return count

# g = int(input('Введите число: '))
# num_digits = number_of_digits_2(g)
# print(f'Количество цифр = {num_digits}.')

# print('28 Подсчитать сумму цифр в числе.')

# def sum_of_digit(number_1): # математ способ
#     count = 0
#     sum = []
#     if number_1 < 0: # проверка на отрицательное число
#         number_1 = abs(- number_1)

#     while number_1 != 0: # формирование массива от введенного числа
#         sum.append(number_1 %10)
#         number_1 //= 10
#         count += 1
    
#     sum_digit = 0 # вычисление суммы чисел
#     for digit in sum:
#         sum_digit += digit
#     print(sum_digit)

# m = int(input('Введите число: '))
# sum_of_digit(m)

# def sum_of_digit_2(number_2): # Решение Семена Овчарова
#     sum_digit = 0
#     for i in number_2:
#         if not (i == '-' or i == '.'):
#             sum_digit += int(i)
#     return sum_digit

# b = input('Введите число: ')
# print(sum_of_digit_2(b))

from math import prod, factorial, pow
# print('29 Написать программу вычисления произведения чисел от 1 до N.')
# def product_of_numbers(segment):
#     multi = 1
#     for i in range(1, segment + 1):
#         print(i, end=' ')
#         multi *= i
#     return multi
    
# n = int(input('Enter namber N: '))
# multi = product_of_numbers(n)
# print(f'The product of numbers = {multi}')

# def product_of_numbers_2(segment):
#     print(f'The product of numbers = {prod(range(1, segment + 1))}')

# n = int(input('Enter namber N: '))
# product_of_numbers_2(n)

# def product_of_numbers_3(n):
#     # return factorial(N)
#     if n == 0: return 1
#     else: return product_of_numbers_3(n-1) * n

# def result_of_prodact(N):
#     for i in (range(1, N + 1)):
#         n = product_of_numbers_3(i)
#     return n

# b = int(input('Enter namber N: '))
# print(result_of_prodact(b))

# print('30 Показать кубы чисел, заканчивающихся на четную цифру.')

# def cubes_of_even_numbers():
#     cub = []
#     for i in range(1, 16): cub.append(pow(i, 3))
#     print('Кубы чисел от 1 до 15: ', cub)
    
#     even_cub = []
#     for i in cub:
#         if i % 2 == 0: even_cub.append(i)
#     print('Кубы чисел, заканчивающихся на четную цифру: ', even_cub)

# cubes_of_even_numbers()
