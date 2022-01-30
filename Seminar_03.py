# Семинар 03 от 27.01.22

from cmath import sqrt
from dataclasses import replace
from itertools import count
from math import ceil, floor, lcm, prod
from random import shuffle, randint
import string

new_text = 'При первом вызове, func (3, 7), параметр a получает значение 9, параметр b \
получает значение 11, а c получает своё значение по умолчанию, равное 10. \
При втором вызове func (25, c=24) переменная a получает значение 26 в силу \
позиции аргумента. После этого параметр c получает значение 23 по имени, \
т.е. как ключевой параметр. Переменная b получает значение по умолчанию, \
равное 5.'

print('31. Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.')

def create_list(N = 12): 
    list_N = [] 
    res = 1
    for i in range(0, N + 1):
        if len(list_N) % 2:
            res = -3 ** i
            list_N.append(res)
        else: 
            res = 3 ** i
            list_N.append(res)
    return list_N

print(create_list())

print('32. Для натурального N создать словарь индекс-значение, \
    состоящий из элементов последовательности 3k + 1.')

def d_N(N):
    dictionary_2 = {k: (3 * k) + 1 for k in range(1, N + 1)}
    dictionary_N = {}
    for k in range(1, N + 1):
        res = (3 * k) + 1
        dictionary_N[k] = res
    return dictionary_N, dictionary_2
    
print(d_N(5))

print('33. Пользователь задаёт две строки. \
    Определить количество вхождений одной строки в другой.')

def the_number_of_occurrences_of_one_string_in_another(s_1, s_2):
    count = 0
    symbol = '' # 
    for i in s_1:
        for j in s_2:
            if i == j:
                count += 1
                symbol += i
    return count, symbol
    
    return s_1.count(s_2)
    
    clear_text  = s_1\
        .lower()\
        .replace(',', '')\
        .replace('(', '')\
        .replace(')', '')\
        .replace('.', '')\
        .replace('  ', ' ') # очистка текста
    list_text = clear_text.split(' ') # split преобразует в лист, а (сепаратор) раздел элементы листа
    for i in list_text:
        if s_2 == i:
            count +=1
    return count

string_1 = input('Введите любое предложение: ')
string_2 = input('Введите еще раз любое предложение: ')
print(the_number_of_occurrences_of_one_string_in_another\
    (string_1, string_2))

print('34. Подсчитать сумму цифр в вещественном числе.')

def sum_digits_in_real_number(real_numb = '-123.123'):
    real_numb = real_numb\
        .replace('-', '')\
        .replace('+', '')\
        .replace('.', '')
    return sum(int(i) for i in real_numb)

print(sum_digits_in_real_number())  

print('35. Написать программу получающую набор произведений чисел от 1 до N.\
    Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ].')

def product_number_of_segment(number = 6):
    list_numbers = []
    product = 1
    for i in range(1, number):
        product *= i
        list_numbers.append(product)
    return list_numbers

print(product_number_of_segment(10))

print('36. Задать список из n чисел последовательности \
      (1+1/n)n и вывести на экран их сумму')

def sum_of_numbers_in_list(n = 4):
    numbers_in_list = [(1 + (1 / i) ** i) for i in range(1, n + 1)]
    print(numbers_in_list) # для наглядности
    return sum(numbers_in_list)

print(sum_of_numbers_in_list(10))

print('37.Задать список из N элементов, заполненных числами из [-N, N]. \
      Найти произведение элементов на указанных позициях. \
      Позиции хранятся в файле file.txt в одной строке одно число .')

# Задать список из N элементов, заполненных числами из [-N, N]
def create_list_number(N = 6): 
    return [i for i in range(-N, N + 1)]
# Позиции хранятся в файле file.txt в одной строке одно число 
def create_text_file(list_N, name_file = 'task_37.txt', mode = 'w'):
    with open(name_file, mode) as data:
        for i in list_N: # элементы
        # for i in range(0, len(list_N)): # индексы
            data.write(f'{i}\n') # аргумент write() должен быть str, а не list
        # j = 0
        # for i in list_N: # индексы и элементы
        #     data.write(f'{j}:{i}\n')
        #     j += 1
    return name_file
# Показ позиций в файле и создание списка из файла (можно без показа)
def show_text_file_and_create_new_list(rd = ''):
    list_N_new = []
    path = rd
    data = open(path, 'r')
    for line in data:
        # print(line) # без показа
        list_N_new.append(int(line))
    data.close()
    return list_N_new
# Найти произведение элементов на указанных позициях
def prodact_number_in_list(lst):
    # return prod(lst) # возвр 0
    product = 1
    for i in lst:
        if i != 0:
            product *= i 
    return product 

list_number = create_list_number()
print(list_number)
new_file = create_text_file(list_number)
new_list = show_text_file_and_create_new_list(new_file)
print(new_list)
print(prodact_number_in_list(new_list))

print('38. Реализовать алгоритм перемешивания списка.')

lst = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
# Штатный
lst = [2, 8, 4, 3, 1, 5]  
shuffle(lst) 
print(lst)

Рабочий
def shuffling_the_list(mixed):
    count = len(mixed) # // 2
    while count >= 0:
        count1 = randint(0, len(mixed)-1)
        temp = mixed[count1]
        mixed.pop(count1)
        mixed.append(temp)
        count -= 1
    return mixed
    
print(shuffling_the_list(lst))

Хромающий
count = len(lst) // 2
while count >= 0:
    count1 = randint(0, len(lst)-1)
    temp = lst[count1]
    lst.insert(count1, lst.pop(temp))
    count -= 1
print(lst)

print('39.Реализовать алгоритм задания случайных чисел. \
      Без использования встроенного генератора псевдослучайных чисел.')

def random_number(rang_s = 1, rang_e = 10):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    quantity = rang_e
    size = len(numbers)
    while quantity == 0:# size

print('40.Определить, присутствует ли в заданном списке строк, некоторое число.')

def find_some_number(Text, find_number):
    # for symbol in Text:
    #     if symbol != find_number:
    #         continue 
    #     else:
    #         return 'The specified number is present'           
    # return 'The specified number is nor present'

    if find_number in Text:
        return True
    else: return False

n = input('Enter number: ')
print(find_some_number(new_text, n))

print('41. Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.')

print('42. Найти сумму чисел списка стоящих на нечетной позиции.')
               0  1  2  3    4  5  6    7  8
simply_list = [3, 1, 7, 56, -3, 5, 89, -9, 11, 4]

def sum_number_in_an_odd_position(l):
    odd_pos = [i for i in range(0, len(l))]
    odd_l = [i for i, j in zip(l, odd_pos) if j % 2 != 0]
    return sum(odd_l)

sum_number = sum_number_in_an_odd_position(simply_list)
print('Summary =', sum_number)

print('43. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, \
        второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15].')
# способ 1
def product_of_pairs_of_numbers_in_list(Li):
    product_of_pairs = [] 
    start_index = 0 
    end_index = len(Li) - 1
    # проверка на разную длину списка, для соблюдения условий задачи
    if len(Li) % 2 != 0: count = - 1
    else: count = 0
    # произведение пар списка
    while count < len(Li) // 2:
        product_of_pairs.append(Li[start_index] * Li[end_index])
        start_index += 1
        end_index -= 1
        count += 1
    return product_of_pairs

prod_list = product_of_pairs_of_numbers_in_list(simply_list)
print(prod_list)

# способ 2
def product_of_pairs_of_numbers_in_list_2(Li):
    new_Li = []
    end_index = len(Li) - 1
    for i in Li:
        new_Li.append(i * Li[end_index])
        end_index -= 1
    if len(new_Li) % 2 != 0: # проверка на разную длину списка, для соблюдения условий задачи
        return new_Li[0:len(new_Li)//2 + 1]
    else: return new_Li[0:len(new_Li)//2]

print(product_of_pairs_of_numbers_in_list_2(simply_list))

print('44. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным\
        значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19.')
real_numbers = [1.1, 1.3, 3.1, 5, 10.012]

def max_and_min_fractional_part(real_lst):
    new_real_list = [round(i - int(i), 4) for i in real_lst]
    max_N = max(new_real_list)
    min_N = new_real_list[0]
    for i in new_real_list:
        if 0 != i < min_N:
            min_N = i
    return max_N - min_N

print(max_and_min_fractional_part(real_numbers))

print('45. Написать программу преобразования десятичного числа в двоичное.')

def converting_decimal_to_binary(decimal_N = 55):
    divider_list = []
    binary_list = []
    while decimal_N != 0:             # создание списка делителей введенного числа
        divider_list.append(decimal_N)
        decimal_N //= 2
    divider_list.reverse()            # реверс списка
    for i in divider_list:            # создание списка остатка от делителей
        binary_list.append(i % 2)
    string = ''                       # преобразования списка в нормальный вид (в строку)
    for i in binary_list:
        string += str(i) + ''
    return string

print(converting_decimal_to_binary())

print('46. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.')

def fibonachi(n):
    if n in [-2, -1, 0, 1, 2]: return 1
    if n > 0: return fibonachi(n - 1) + fibonachi(n - 2) не раб с отриц
    if n < 0: return ((-1) ** n + 1) * (fibonachi(n - 1) + fibonachi(n - 2))

def list_of_number_fibonachi(s_N, e_N):
    number_fibonachi = []
    for i in range(s_N, e_N, -1):
        number_fibonachi.append(fibonachi(i))    
    return number_fibonachi

start_number = int(input('Введите начальное число: '))
end_number = int(input('Введите конечное число: '))
lst_fibo = list_of_number_fibonachi(start_number, end_number)
print(lst_fibo)

def fibonachi_2(N = 100):
    fib = [0, 1]
    for i in range(0, N - 1):
        fib.append(fib[i] + fib[i - 1])
    return fib

print(fibonachi_2())

memo_fib = {1: 0, 2: 1}
def fibonachi_3(number):
    if number in range(0, 1): 
        return number
    if number not in memo_fib:
        memo_fib[number] = fibonachi_3(number \
            - 1) + fibonachi_3(number - 2)
    return memo_fib[number]

fibonachi_3(100)
print(memo_fib)

print('47. Строка содержит набор чисел. Показать большее и меньшее число.')

def larger_and_smaller_numbers_in_row(row_number):
    number_list = []
    for i in row_number:
        int_s = int(i)
        number_list.append(int_s)
    max_N = max(number_list)
    min_N = min(number_list)
    return max_N, min_N
set_numbers = input('Введите подряд нескольно чисел: ')
more, less = larger_and_smaller_numbers_in_row(set_numbers)
print(f'max - {more}, min - {less}')

print('48. Найти корни квадратного уравнения Ax² + Bx + C = 0\
        Математикой\
        Используя дополнительные библиотеки*')

def find_roots_of_quadratic_equation(A, B, C):
    discriminant = (B ** 2) - 4 * A * C
    # discriminant = pow(B, 2) - 4 * A * C
    if discriminant < 0:
        print(f'Дискриминант: {discriminant} < 0, у квадратного уравнения корней нет.')
    elif discriminant == 0:
        X = -B / (2 * A)
        print(f'Дискриминант: {discriminant} = 0, у квадратного уравнения, корень один и равен {X}.')
    else:
        # X1 = (-B - sqrt(discriminant)) / (2 * A) # ???Почему не округляет при таком способе решения тип complex не определяет метод __round__
        # X2 = (-B + sqrt(discriminant)) / (2 * A)
        X1 = (-B - (discriminant ** 0.5)) / (2 * A)
        X2 = (-B + (discriminant ** 0.5)) / (2 * A)

        print(f'Дискриминант: {discriminant} > 0, у квадратного уравнения,\
             два корня {round(X1, 4)} и {round(X2, 4)}.')

a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))
find_roots_of_quadratic_equation(a, b, c)    

print('49. Найти НОК двух чисел')

def smallest_common_multiple(a, b):
    noc = lcm(a, b)
    print('НОК 1 =', noc)
    c, d = a, b
    while a != b:
        if a > b: a -= b
        else: b -= a    
    nod_1 = b
    print('НОД =', nod_1) 
    noc_2 = round((c*d) / nod_1)
    print('НОК 2 =', noc_2)

A = int(input('Введите число А: '))
B = int(input('Введите число B: '))
smallest_common_multiple(A, B)

exit()
print('50. Вычислить число c заданной точностью d. \
    Пример: при d = 0.001, пи = 3.141. 10^-1 <= d >= 10^-10')

print('51. Составить список простых множителей натурального числа N')
