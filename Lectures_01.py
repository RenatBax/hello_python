# print('Hello world')

# Типы данных и переменные

# #int, float, boolean, str
# value = None # для того чтобы использовать эту переменную в дальнейшем, просто value работать не будет
# print(type(value))
# a = 123
# b = 1.23
# print(a)
# print(type(a)) # type чтобы узнать тип данных
# print(b)
# print(type(b))
# value = 12345 
# print(value)
# s = 'qwert'
# print(s) # вывод строки
# d = "Hello 'world'"
# print(d)
# o = 'hello "Mike"'
# print(o)
# r = 'hello \"Mike"'
# print(r)
# t = "Hello \n'world'" #  \n перевод на новую строку
# print(t)

# # Интерполяция

# j = 123
# l = 1.23
# m = 'hello'
# print(j, l, m)
# print( j, '-', l, '-', m)
# #                           0  1  2
# print('{} - {} - {}'.format(j, l, m)) 
# print('{1} - {2} - {0}'.format(j, l, m)) 
# print(f'{j} + {l} + {m}')
# h = False
# print(h)

# # Списки (массивы)

# list = []
# print(list)
# list_2 = [1, 2, 3, 5]
# print(list_2)
# list_3 = ['1', '2', '3', 'hello']
# print(list_3)
# list_4 = ['1', '2', '3', 'hello', 1, 5, 675, 2.34, True] # можно даже так, но не нужно)
# # чувствителен к пробелам, работать не будет
# print(list_4) 

# # Ввод и вывод данных

# # print() вывод данных
# # input() ввод данных
# print('Enter q')
# q = input()
# print('Enter p')
# p = input()
# print(q, '+' , p, '=', q + p) # не будет работать не указан тип вводимых данных 
# print('Enter i')
# i = int(input()) # для этого нужно указать тип данных таким образом
# print('Enter w')
# w = int(input())
# print(i, '+' , w, '=', i + w)

# Арифметические операции

# +, -, *, /, %, //, **

from tkinter import N

a = 6
b = 5 # -5 унарный минус и есть унарный плюс
c = a + b
print(c)
h = a - b
print(h)
u = a * b
print(u)
o = a / b
print(o)
i = a % b # остаток от деления
print(i)
p = a // b # деление в целых числах
print(p)
y = a ** b # возведение в степень
print(y)
c = 1.35678
z = 3
g = c * z # округляет по математ правилам
print(g)
t = round(c * z) # округляет по математ правилам
print(t)
v = round(c * z, 2) # округляет по указанной цифре после запятой 
print(v)

# сокращенные арифм операции присваивания
# +=, -=, *=, /=

r = 3
# r = r + 5
r += 5
print(r)

# Логические операции
# сравнения >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# gen

u = 1 > 4
print(u)
c = 1 < 4 and 5 > 2
print(c)

l = 'try'
k = 'tryy'
print(l != k)

t = [1, 4]
f = [1, 3]
print(t < f)

s = 1 < 4 < 5 # тройные и больше не равенства
print(s)

func = 1
T = 4
x = 123
print(func<T>(x))

fun = 1 > 2 or 4 < 6 #дизьюнкция
print(fun)

# is, is not, in, not in
R = [1, 2, 3, 4]
print(R)
print(2 in R) # 2 есть в R???
print(not 2 in R) # наоборот

is_odd = f[0] % 2 == 0 # остаток от деления равет 0
is_odd2 = not f[0] % 2 # можно записать так - пайтоновский вариант записи
print(is_odd)
print(is_odd2)

# Управляющие конструкции, важны отступы

# if
# d = int(input('a = '))
# g = int(input('b = '))
# if d > g:
#     print(d)
# else:
#     print(g)

# if-else
# username = input('Введите имя: ')
# if username == 'Masha':
#     print('Ура, это же Маша!')
# elif username == 'Marina':
#     print('Я так Вас ждал, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Hello, ', username)

# while
# original = 2357
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)
# print()

# # while-else
# original = 2357986
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй \nхватит')
#     print('Ну')
#     print('хватит )')
# print(inverted)

# # for
# list = [1, 2, 4, 5, 6]
# for i in list:
#     print(f'{i} - {i ** 2}')

# r = range(10) # от 0 до 9
# for j in r:
#     print(j)

# for o in range(-2, 6): # от -2 до 5
#     print(o)
   
# for l in range(5, 15, 3): # 3 задает с какой переодичностью ранжир цифры в указанном диапазоне
#     print(l)

# for k in 'qwerty':
#     print(k)

#
# text = 'съешь еще этих мягких французских булок'
# print(len(text)) #   len - длина
# print('еще' in text) # проверка подстроки в строке
# print(text.isdigit()) # 
# print(text.islower()) # регистр букв нижний
# print(text.replace('еще', 'ЕЩЕ')) #  replece - замена

# for c in text:
#     print(c)

# подсказки 
# str. поставить точку после покажет варианты применения других функций методов
# любой непонятный метод, тип данных можно узнать вызвав команду
# help(str) Q - выйти из справки

# Cрезы - работа с текстом
#       0                                     -1
# text = 'съешь еще этих мягких французских булок'
# print(text[0])                  # c
# print(text[1])                  # ъ
# #print(text[len(text)])          # ощибка из-за индексации с 0
# print(text[len(text) - 1])      # к
# print(text[-5])                 # б
# print(text[:])                  # синтаксический сахар
# print(text[0: len(text) - 1])       # print(text[:])
# print(text[len(text) - 2:])     # ок
# print(text[2:9])                # ешь еще
# print(text[6:-18])              # еще этих мягких
# print(text[0:len(text):6])      # сеикакл
# print(text[::6])                # сеикакл
# text = text[2:9] + text[-5] + text[:2] #

# Списки - введение
numbers = [1, 2, 3, 4, 5]  # [1, 2, 3, 4, 5]
print(numbers) 
ran = range(1, 6)
print(type(ran)) # <class 'range'>
numbers = list(ran) # приведение типа данных renge  к list
print(type(numbers))  # <class 'list'>
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
print(f'{len(numbers)} len') # 5 len
for i in numbers:
    i *= 2   
    print(i)   # [20 4 6 8 10] по строчно
print(numbers) # [10, 2, 3, 4, 5] изменения строкой выше не сохраняются при вызове списка

colors = ['red', 'green', 'blue']

for e in colors:
    print(e) # red green blue

for e in colors: 
    print(e * 2) # redred greengreen blueblue

colors.append('grey') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) #
colors.remove('red') # del colors[0] # удалить элемент

# Функции
# def function_name(x):
#     body line 1
#     ......
#     body line N
#     optional return

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 56
print(f(arg))
print(type(f(arg)))