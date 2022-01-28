# Семинар_01

print('Задача 0. Вывести квадрат числа.')

number = int(input('Введите число: '))
print(f'Квадрат введенного числа {number} равен {number ** 2}')

print('3адача 1. По двум заданным числам проверять является ли первое квадратом второго.')

def sqrt_numbers(a, b):
    if a ** 2 == b:
        print(f'Первое число является квадратом второго: {a}x2 = {b}.')
    else:
        print('Первое число не является квадратом второго.')

print('По двум введенным числам проверьте, является ли первое квадратом второго?')
sqrt_numbers(a = int(input('Введите первое число: ')), b = int(input('Введите второе число: ')))

print('3адача 2. Даны два числа. Показать большее и меньшее число.')

def max_number(c, d):
    if c > d:
        return f'{c} - большее число, а {d} меньшее.'
    if c < d:
        return f'{d} - большее число, а {c} меньшее.'
    else:
        return 'Числа равны.'

print(max_number(c = int(input('Введите первое число: ')), d = int(input('Введите второе число: '))))

print('3адача 3. По заданному номеру дня недели вывести его название.')

def show_day_of_week(day): # работает
    week = range(1, 8)
    days = list(week)
    for i in days:
        if day == days[0]:
            print('понедельник')
            break
        elif day == days[1]:
            print('вторник')
            break
        elif day == days[2]:
            print('среда')
            break
        elif day == days[3]:
            print('четверг')
            break
        elif day == days[4]:
            print('пятница')
            break
        elif day == days[5]:
            print('суббота')
            break
        elif day == days[6]:
            print('воскресенье')
            break
        else:
            print('Такого дня не существует.')
            break

show_day_of_week(day = int(input('Введите день недели: ')))

print('3адача 4. Найти максимальное из трех чисел.')

def max_of_3_numbers(a1, a2, a3):
    ''' Программа находит максимальное из трех чисел. 

        Это пример написания документации к задаче.
        Пишется до выполнения логических операций.
        Документация начинается и заканчивается тремя кавычками, не забываем про табуляцию! 
        Каждое предложение на строчке нач с загл буквы и окон точкой.
        Между первым и вторым предложением - пустая строчка.
                                  имя функции точка  команда
        Выводится командой print(max_of_3_numbers.__doc__).'''
    if a2 < a1 > a3:
        return f'Max number {a1}.'
    elif a1 < a2 > a3:
        return f'Max number {a2}.'
    elif a1 < a3 > a2:
        return f'Max number {a3}.'
    else:
        return f'The entered numbers are equal to, max {a1 or a2 or a3}'

print(max_of_3_numbers(a1 = int(input("Enter the first number: ")), # вывод 1 способ
                        a2 = int(input("Enter the second number: ")),
                        a3 = int(input("Enter the third number: "))))
print(max_of_3_numbers.__doc__)

result = max_of_3_numbers(a1 = int(input("Enter the first number: ")), # Второй способ вывода
        a2 = int(input("Enter the second number: ")),
        a3 = int(input("Enter the third number: ")))
print(result)       

print('Решение 4 задачи вторым способом')

def max_of_3_numbers_2():
    nambers = []
    count = 1
    while count <= 3:
        enter_number = int(input(f'Enter {count} number: '))
        nambers.append(enter_number)
        count = count + 1
    nambers # список введенных чисел
    max_number = nambers[0]
    for i in nambers:
        if i > max_number: max_number = i # находим мах
    return max_number

search_number = max_of_3_numbers_2()
print(f'Max number {search_number}')

print('3адача 5. Написать программу вычисления значения функции y = f(a) y=sin(x^10)') 

def calculate_the_value_of_the_function(x):
    import math
    y = round(math.sin(x ** 10), 4)
    return y

y = calculate_the_value_of_the_function(x = int(input('Для вычисления значения функции y=sin(x^10), введите число х: ')))
print('y = sin(x^10) =', y)

print('3адача 6. Выяснить является ли число чётным')

def event_number(event_not_event):
    if event_not_event % 2 == 0:
        return print('Число четное')
    else:
        return print('Число нечетное')

event_number(event_not_event = int(input('Введите число: ')))

print('3адача 7. Показать числа от -N до N')

def show_numbers_from_N_to_N(N):
    segment = []
    for i in range(-N, N + 1):
        segment.append(i)
    print(segment)

show_numbers_from_N_to_N(N = int(input('Введите число N: ')))

print('3адача 8. Показать четные числа от 1 до N')

event_from_segment = int(input('Введите число: '))
for i in range(1, event_from_segment + 1):
    if i % 2 == 0:
        print(i)

print('3адача 9. Показать последнюю цифру трёхзначного числа')

def last_number(number):
    digit = number - (number - number%10)
    print(f'The last digit of a three-digit number: {digit}.')

last_number(number = int(input('Enter three-digit number: ')))

print('3адача 10. Показать вторую цифру трёхзначного числа')

def show_numbers(num):
    second_digit = num // 10 % 10
    return second_digit

second_digit = show_numbers(num = int(input('Enter three-digit number: ')))
print(f'The second digit of a three-digit number: {second_digit}.')

print('3адача 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа')

from random import randint

def get_random_number():
    return randint(10, 100)

random_number = get_random_number()

def max_digit(number):
    if number[0] > number[1]:
        print('Max digit of the number =', number[0])
    elif number[0] < number[1]:
        print(f'Max digit of the number = {number[1]}.')
    else:
        print('The digits of the number are equal.')

print(f'Given a number {random_number} from the segment [10, 99]')
max_digit(number = str(random_number))

print('Решение 11 задачи вторым способом')
def max_digit_math_way(n):
    digit_2 = []
    digit_2.append(n % 10)
    digit_1 = []
    digit_1.append(n // 10)
    
    if digit_1[0] > digit_2[0]: return digit_1[0]
    elif digit_1[0] < digit_2[0]: return digit_2[0]
    else: return 'Digit are equal'
max_digit_2 = max_digit_math_way(random_number)
print(f'Max digit of the number: {max_digit_2}.')

print('Решение 11 задачи третьим способом (NataSola)') 
def max_digit_math_way_2(n):  
    if n // 10 > n % 10: 
        return n //10
    elif n // 10 < n % 10: 
        return n % 10
    else: return 'Digit are equal.'

max_digit_3 = max_digit_math_way_2(random_number)
print(f'Max digit of the number: {max_digit_3}.')

print('3адача 12. Удалить вторую цифру трёхзначного числа')

def delete_digit_string_metod(sn):
    for i in sn:
        if i == sn[2]:
            print(f'{sn[0]}{sn[2]}')
            break
        elif i > sn[2]:
            print(f'{sn[1]}{sn[3]}')
            break

delete_digit_string_metod(sn = input('Введите трехзначное число: '))

print('Решение 12 задачи вторым способом')
def delete_number_math_metod(m):
    digit3 = m % 10
    digit1 = m // 100
    print(digit1 * 10 + digit3)

delete_number_math_metod(m = int(input('Второй способ. Введите трехзначное число: ')))

print('3адача 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.')

user_number = int(input('Enter a number: '))
from random import randint
specified_number = randint(1, 100)
print(f'The specified number = {specified_number}')

def multiple_number(s, u):
    result = round(s / u, 2)
    remains = s % u
    print('As a result of division', result)
    if result%2 == 0:
        print('The entered number is a multiple of the specified one')
    else:
        print(f'The entered number is NOT a multiple of the specified one - remains ({remains}).')

multiple_number(specified_number, user_number)

print('3адача 14. Найти третью цифру числа или сообщить, что её нет')

def is_there_third_digit(text): # не работает с отрицательными
    
    if len(text) >= 3:
        print(f'Третья цифра есть, {text[2]}')
    else:
        print('Третьей цифры в числе нет.')

is_there_third_digit(text = input('Введите число: '))

print('Решение 14 задачи вторым способом')

import math
def is_there_third_digit2(number1):
    if number1 > 99 or number1 < -99:
        if number1 < 0:
            digit = abs(-number1) // 100 % 10
        else:
            digit = number1 // 100 % 10
        print(f'Третья цифра = {digit}.')
    else:
        print('Третьей цифры в числе нет.')

is_there_third_digit2(number1 = int(input('Введите число: ')))

print('3адача 15. Дано число. Проверить кратно ли оно 7 и 23')

def multiple_of_seven_and_twentythree(numb):
    if numb % 7 == 0 and numb % 23 == 0:
        print('The entered number is multiple of 7 and 23')
    else:
        print('The entered number is not multiple of 7 and 23')

multiple_of_seven_and_twentythree(numb = int(input('Enter a number: ')))

print('3адача 16. Дано число обозначающее день недели. Выяснить является номер дня недели выходным')

def weekend():
    from random import sample
    from time import sleep
    a_week = sample(range(1, 8), 1)
    for day in a_week:
        print(f'Дано число обозначающее день недели {day}.')
        sleep(2)
        if day <= 5:
            print('Вам не повезло, рабочий день')
        elif day == 6 or day == 7:
            print('Ура! Выходной день!')
weekend()
