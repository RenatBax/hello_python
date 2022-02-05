# Семинар 04 31.01.2022

from math import pi, sqrt
from Seminar_03 import new_text

# print('41. Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.')

# def clear_any_text(text_old):
#     text_new  = text_old\
#         .lower()\
#         .replace(',', '')\
#         .replace('(', '')\
#         .replace(')', '')\
#         .replace('.', '')\
#         .replace('  ', ' ') # очистка текста
#     return text_new

# def position_of_second_occurrence_string_in_list(s_1, s_2):

#     str_1 = clear_any_text(s_1).split(' ') # split преобразует в лист, а (сепаратор) раздел элементы листа
#     str_2 = clear_any_text(s_2)
#     contain = 0
#     pos = 0
#     for i in range(0, len(str_1)):
#         temp = str_1[i]
#         if str_1[i] == str_2:
#             contain += 1
#             pos = i
#     if contain == 2: return f'Позиция второго вхождения = {pos}.'
#     else: return f'Первое = {pos}. Второго вхождения строки в списке нет.'

# string_2 = input('Введите любое предложение: ')
# print(position_of_second_occurrence_string_in_list\
#     (new_text, string_2))

# lst = ['sdf', 'serwerjhsd', 'sd234345', 'sdfsd', 'sdfsdf']
# sub_str = 'sdf'
# in_list = 0
# for i , item in enumerate(lst):
#     pos = item.find(sub_str)
#     if pos != -1:
#         in_list += 1
#     if in_list == 2:
#         print(i)

# print('42. Найти сумму чисел списка стоящих на нечетной позиции.')
#                0  1  2  3    4  5  6    7  8
# simply_list = [3, 1, 7, 56, -3, 5, 89, -9, 11, 4]

# def sum_number_in_an_odd_position(l):
#     odd_pos = [i for i in range(0, len(l))]
#     odd_l = [i for i, j in zip(l, odd_pos) if j % 2 != 0]
#     return sum(odd_l)

# sum_number = sum_number_in_an_odd_position(simply_list)
# print('Summary =', sum_number)

# print(sum([item if i % 2 else 0 for i, item in enumerate(simply_list)])) 

# print('43. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, \
#         второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15].')
# # способ 1
# def product_of_pairs_of_numbers_in_list(Li):
#     product_of_pairs = [] 
#     start_index = 0 
#     end_index = len(Li) - 1
#     # проверка на разную длину списка, для соблюдения условий задачи
#     if len(Li) % 2 != 0: count = - 1
#     else: count = 0
#     # произведение пар списка
#     while count < len(Li) // 2:
#         product_of_pairs.append(Li[start_index] * Li[end_index])
#         start_index += 1
#         end_index -= 1
#         count += 1
#     return product_of_pairs

# prod_list = product_of_pairs_of_numbers_in_list(simply_list)
# print(prod_list)

# # способ 2
# def product_of_pairs_of_numbers_in_list_2(Li):
#     new_Li = []
#     end_index = len(Li) - 1
#     for i in Li:
#         new_Li.append(i * Li[end_index])
#         end_index -= 1
#     if len(new_Li) % 2 != 0: # проверка на разную длину списка, для соблюдения условий задачи
#         return new_Li[0:len(new_Li)//2 + 1]
#     else: return new_Li[0:len(new_Li)//2]

# print(product_of_pairs_of_numbers_in_list_2(simply_list))

# list_len = len(simply_list)
# print([simply_list[i] * simply_list[list_len - i - 1] for i in range(0, list_len // 2 + 1)])

# print('44. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным\
#         значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19.')

# real_numbers = [1.13, 1.34, 3.001, 5, 10.012]

# def max_and_min_fractional_part(real_lst):
#     new_real_list = [round(i - int(i), 4) for i in real_lst]
#     max_N = max(new_real_list)
#     min_N = new_real_list[0]
#     for i in new_real_list:
#         if 0 != i < min_N:
#             min_N = i
#     return max_N - min_N

# print(max_and_min_fractional_part(real_numbers))

# float_list = [round(item % 1, 2) for item in real_numbers]
# print(float_list)
# print(f'{max(float_list) - min(float_list) : .2f}'

# print('45. Написать программу преобразования десятичного числа в двоичное.')

# def converting_decimal_to_binary(decimal_N = 55):
#     divider_list = []
#     binary_list = []
#     while decimal_N != 0:             # создание списка делителей введенного числа
#         divider_list.append(decimal_N)
#         decimal_N //= 2
#     divider_list.reverse()            # реверс списка
#     for i in divider_list:            # создание списка остатка от делителей
#         binary_list.append(i % 2)
#     string = ''                       # преобразования списка в нормальный вид (в строку)
#     for i in binary_list:
#         string += str(i) + ''
#     return string

# print(converting_decimal_to_binary())

# print('46. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.')

# def fibonachi(n):
#     if n in [0, 1]: return 1
#     if n > 0: return fibonachi(n - 1) + fibonachi(n - 2) 
#     if n < 0: return (fibonachi(n + 2) - fibonachi(n + 1))

# def list_of_number_fibonachi(s_N, e_N):
#     number_fibonachi = []
#     for i in range(s_N - 1, e_N):
#         number_fibonachi.append(fibonachi(i))    
#     return number_fibonachi

# start_number = int(input('Введите начальное число: '))
# end_number = int(input('Введите конечное число: '))
# lst_fibo = list_of_number_fibonachi(start_number, end_number)
# print(lst_fibo)

# def fibonachi_2(N = 100):
#     fib = [0, 1]
#     for i in range(0, N - 1):
#         fib.append(fib[i] + fib[i - 1])
#     return fib

# print(fibonachi_2())

# memo_fib = {1: 0, 2: 1}
# def fibonachi_3(number):
#     if number in range(0, 1): 
#         return number
#     if number not in memo_fib:
#         memo_fib[number] = fibonachi_3(number \
#             - 1) + fibonachi_3(number - 2)
#     return memo_fib[number]

# fibonachi_3(100)
# print(memo_fib)

# print('47. Строка содержит набор чисел. Показать большее и меньшее число.')

# def larger_and_smaller_numbers_in_row(row_number):
#     number_list = []
#     for i in row_number:
#         int_s = int(i)
#         number_list.append(int_s)
#     max_N = max(number_list)
#     min_N = min(number_list)
#     return max_N, min_N
# set_numbers = input('Введите подряд нескольно чисел: ')
# more, less = larger_and_smaller_numbers_in_row(set_numbers)
# print(f'max - {more}, min - {less}')

# print('48. Найти корни квадратного уравнения Ax² + Bx + C = 0\
#         Математикой\
#         Используя дополнительные библиотеки*')

# def find_roots_of_quadratic_equation(A, B, C):
#     discriminant = (B ** 2) - 4 * A * C
#     # discriminant = pow(B, 2) - 4 * A * C
#     if discriminant < 0:
#         print(f'Дискриминант: {discriminant} < 0, у квадратного уравнения корней нет.')
#     elif discriminant == 0:
#         X = -B / (2 * A)
#         print(f'Дискриминант: {discriminant} = 0, у квадратного уравнения, корень один и равен {X}.')
#     else:
#         # X1 = (-B - sqrt(discriminant)) / (2 * A) # ???Почему не округляет при таком способе решения тип complex не определяет метод __round__
#         # X2 = (-B + sqrt(discriminant)) / (2 * A)
#         X1 = (-B - (discriminant ** 0.5)) / (2 * A)
#         X2 = (-B + (discriminant ** 0.5)) / (2 * A)

#         print(f'Дискриминант: {discriminant} > 0, у квадратного уравнения,\
#              два корня {round(X1, 4)} и {round(X2, 4)}.')

# a = int(input('Введите число А: '))
# b = int(input('Введите число B: '))
# c = int(input('Введите число C: '))
# find_roots_of_quadratic_equation(a, b, c)    

# print('49. Найти НОК двух чисел')

# def great_common_div(number_1, number_2):
#     if number_1 == number_2: return number_1
#     elif number_1 > number_2: return great_common_div(number_1 - number_2, number_2)
#     elif number_1 < number_2: return great_common_div(number_1, number_2 - number_1)

# def smallest_common_multiple(a, b):
#     # noc = lcm(a, b) # с использ библиотеки
#     # print('НОК 1 =', noc)

#     # c, d = a, b способ 1
#     # while a != b:
#     #     if a > b: a -= b
#     #     else: b -= a    
#     # nod_1 = b
#     # noc_2 = round((c*d) / nod_1)
#     # print('НОК 2 =', noc_2)

#     nod = great_common_div(a, b) # способ 2 с использованием рекурсии
#     noc_3 = (a * b) // nod
#     print('НОК 3 =', noc_3)

# A = int(input('Введите число А: '))
# B = int(input('Введите число B: '))
# smallest_common_multiple(A, B)

# print('50. Вычислить число c заданной точностью d. \
#     Пример: при d = 0.001, пи = 3.141. 10^-1 <= d >= 10^-10')

# def specified_accuracy(real_numb):
#     d = '0.000'
#     d = int(len(d) - 2)
#     accuracy_number = round(real_numb, d)
#     return accuracy_number

# n = float(input('Введите любое вещественное число: '))
# t = specified_accuracy(n)
# print(t)

# real_numb = -12345.45678789946896666
# print(f'{real_numb}')
# print(f'{real_numb:.3f}')

# def round2(real_numb, d = 3):
#     disc_round = \
#         {
#             1: 0.1,
#             2: 0.01,
#             3: 0.001,
#             4: 0.0001,
#             5: 0.00001,
#             6: 0.000001,
#             7: 0.0000001,
#             8: 0.00000001,
#             9: 0.000000001,
#             10: 0.0000000001
#         }

#     kf = disc_round[d]
#     s_r_n = str(real_numb / kf)
#     idx = s_r_n.find('.')
#     i_r_n = int(s_r_n[:idx])
#     round_number = i_r_n * kf
#     return round_number

# print(round2(pi, 3))

# print('51. Составить список простых множителей натурального числа N')

# def get_simple_list():
#     N = sqrt(30000)
#     list_prime_number = []
#     list_number = [number for number in range(2, int(N) + 1)]
#     for number in list_number:
#         for i in range(2, number):
#             if not number % i: break
#         else: list_prime_number.append(number)
#     return list_prime_number

# def binary_searсh(any_list, any_number):
#     idx = 0
#     size = len(any_list)
#     while idx != size:
#         search = (idx + size) // 2
#         if any_number == any_list[search]: return True
#         if any_number < any_list[search]: size = search
#         else: idx = search + 1
#     return False

# def list_of_prime_factors_of_natural_number(N):
#     prime_factors = []
#     list_prime = get_simple_list() 
#     res = binary_searсh(list_prime, N)
#     if res == True: prime_factors.append(N)
#     else:
#         for i in list_prime:
#             while not N % i:
#                 N /= i
#                 prime_factors.append(i)
#             if N == 1: break 
    
#     if N > list_prime[-1]: prime_factors.append(int(N)) 
#     return prime_factors

# n = 61567
# print(list_of_prime_factors_of_natural_number(n))
