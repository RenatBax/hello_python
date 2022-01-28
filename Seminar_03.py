# Семинар 03 от 27.01.22
from itertools import count
from math import prod
from random import shuffle, randint

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
    dictionary_N = {}
    for k in range(1, N + 1):
        res = (3 * k) + 1
        dictionary_N[k] = res
    return dictionary_N
    
print(d_N(5))

print('33. Пользователь задаёт две строки. \
    Определить количество вхождений одной строки в другой.')

def the_number_of_occurrences_of_one_string_in_another(s_1, s_2):
    count = 0
    symbol = ''
    for i in s_1:
        for j in s_2:
            if i == j:
                count += 1
                symbol += i
    return count, symbol

string_1 = input('Введите любое предложение: ')
string_2 = input('Введите еще раз любое предложение: ')
print(the_number_of_occurrences_of_one_string_in_another\
    (string_1, string_2))

print('34. Подсчитать сумму цифр в вещественном числе.')

def sum_digits_in_real_number(real_numb = '-234.654'):
    sum_digits = 0
    for symbol in real_numb:
        if not (symbol == '-' or symbol == '.'):
            sum_digits  += int(symbol)
    return sum_digits

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

new_text = 'При первом вызове, func(3, 7), параметр a получает значение 9, параметр b\
            получает значение 11, а c получает своё значение по умолчанию, равное 10.\
            При втором вызове func(25, c=24) переменная a получает значение 26 в силу\
            позиции аргумента. После этого параметр c получает значение 23 по имени,\
            т.е. как ключевой параметр. Переменная b получает значение по умолчанию,\
            равное 5.'

def find_some_number(Tt, find_number):
    for symbol in Tt:
        if symbol != find_number:
            continue 
        else:
            return 'The specified number is present'
            
    return 'The specified number is nor present'

n = input('Enter number: ')
print(find_some_number(new_text, n))

print('41. Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.')

print('42. Найти сумму чисел списка стоящих на нечетной позиции.')

print('43. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, \
        второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15].')

print('44. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным\
        значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19.')

print('45. Написать программу преобразования десятичного числа в двоичное.')

print('46. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.')

print('47. Строка содержит набор чисел. Показать большее и меньшее число.')

print('48. Найти корни квадратного уравнения Ax² + Bx + C = 0\
        Математикой\
        Используя дополнительные библиотеки*')

print('49. Найти НОК двух чисел')

print('50. Вычислить число c заданной точностью d. \
    Пример: при d = 0.001, пи = 3.141. 10^-1 <= d >= 10^-10')

print('51. Составить список простых множителей натурального числа N')