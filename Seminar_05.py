# Семинар 5 от 03.02.2022
from random import randint


# 52. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

sequence_of_numbers = '1 2 4 3 87 33 5 2 8 15 2 23 56 87 7 1 38'.split() 
# # unique = map(int, sequence_of_numbers)
# list_unique = list(set(map(int, sequence_of_numbers)))
# print(list_unique)
# # list_unique.sort()
# # print(f'{list_unique}')

# seq_list = [int(i) for i in sequence_of_numbers]
# s = list(filter(lambda x, y: x != y, [j for i, j in seq_list]))
# print(s)

# 53. Задана натуральная степень k. Сформировать случайным образом список коэффициентов \
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. \
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
def write_file(file_name, data):
    with open(file_name, 'w') as file_1:
        file_1.write(data)

def read_file(file_name):
    with open(file_name, 'r') as data:
        return data.read() + ' '
        
# def list_of_coefficients_of_polynomial(k = 4):
#     l_poli = []
#     s = ''
#     coeff = [randint(0, 100) for _ in range(k)]
#     if k >= 2:
#         for i in range(2, len(coeff)):
#             if coeff[i] != 0 and coeff[i] != 1:
#                 l_poli.append(str(coeff[i]) + '*x^' + str(i))
#     if coeff[1] != 0 or coeff[1] != 1: l_poli.append(str(coeff[1]) + '*x')
#     if coeff[0] != 0 or coeff[0] != 1: l_poli.append(str(coeff[0]))
#     for i in l_poli[:-1]:
#         s += i + ' + '
#     s += l_poli[-1] + ' = 0'
#     name = 'task_53.txt'
#     write_file(name, s)

# list_of_coefficients_of_polynomial()

# 54. Даны два файла в каждом из которых находится запись многочлена. \
# Сформировать файл содержащий сумму многочленов.
# m1 = '5*x^2 + 9*x - 5 = 0'
# n1 = 'task_54.1.txt'
# write_file(n1, m1)

# def summary_polinomial(file_1 = 'task_53.txt', file_2 = 'task_54.1.txt'):
#     data1 = read_file(file_1)
#     data2 = read_file(file_2)
#     d1, d2 = data1[:-5], data2[:-5]
#     d = d1 + d2
#     print(f'({d1}) + ({d2})')

# summary_polinomial()

# 55. В файле находится N натуральных чисел, записанных через пробел. \
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
# m2 = '1 2 3 4 5 7 8'
# n2 = 'task_55.txt'
# write_file(n2, m2)

# def find_number(n2):
#     dat = read_file(n2)
#     A = list(map(int, dat.split()))
#     find_numb = [A[i] - 1 for i in range(1, len(A)) if A[i] - 1 != A[i - 1]]
#     return str(find_numb)

# print(find_number(n2))

# 56. Дан список чисел. Выделить среди них числа, удовлетворяющие условию: \
# следующее больше предыдущего. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] \
# или [1, 7] или [1, 6, 7] и т.д.

task_list = [1, 5, 2, 3, 4, 6, 1, 7]

# new = [res for idx, res in enumerate(task_list) if task_list[idx] -1 > task_list[idx - 1]]
# print(new)

def sort_max(task_list):
    sort_list = []
    max = task_list[0]
    for i in task_list:
        if i > max or max < i + 1:
            max = i
            sort_list.append(max) 
    return sort_list

print(sort_max(task_list))


# 57. Дан список чисел. Выделить среди них максимальное количество чисел, \
# удовлетворяющих условию предыдущей задачи. \
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# new = [i for i in task_list if i <= i + 1]
# print(new)

# new = list(filter(lambda x: x + 1 > x and not x >= x + 2, task_list))
# print(new)

# 58. Напишите программу, удаляющую из текста все слова содержащие "абв".

given_text = 'енот проабв из вепщк абвпро если аб не равно бв'
word = 'абв'

# def delete_words(given_text, search_word):
#     count = 0
#     u = 0
#     if given_text.endswich(search_word):
#         print(given_text)
#     if given_text.startswich(search_word):
#         print(given_text)

# delete_words(given_text, word)

# print(given_text)
# # if 'абв' in given_text.replace('абв', ''):
# n = given_text.replace('абв', '')
# print(n)

# 59. Помните игру с конфетами из модуля "Математика и Информатика"? \
# Создайте такую игру для игры человек против человека
    # Добавьте игру против бота
    # Подумайте как наделить бота "интеллектом" 

# 60. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

# 61. Написать программу вычисления арифметического выражения заданного строкой. \
# Используются операции +,-,/,*. приоритет операций стандартный. \
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -6; 
# Добавить возможность использования скобок, меняющих приоритет операций. \
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

# 62. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных файлах
