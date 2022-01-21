# 0. Вывести квадрат числа

# number = int(input('Введите число: '))
# print(f'Квадрат числа {number} равен {number ** 2}')

#1. По двум заданным числам проверять является ли первое квадратом второго

# def sqrtNumbers(a, b):
#     if a ** 2 == b:
#         print(f'Первое число является квадратом второго: {a}x2 = {b}')
#     else:
#         print('Первое число не является квадратом второго')

# print('По двум заданным числам проверьте, является ли первое квадратом второго?')

# sqrtNumbers(a = int(input('Введите первое число: ')), b = int(input('Введите второе число: ')))

# 2. Даны два числа. Показать большее и меньшее число

# def maxNumber(a, b):
#     if a > b:
#         return f'{a} - большее число, а {b} меньшее.'
#     if a < b:
#         return f'{b} - большее число, а {a} меньшее.'
#     else:
#         return 'Числа равны.'

# print(maxNumber(a = int(input('Введите первое число: ')), b = int(input('Введите второе число: '))))

# 3. По заданному номеру дня недели вывести его название

# def show_day_of_week(day): # работает
#     week = range(1, 8)
#     days = list(week)
#     for i in days:
#         if day == days[0]:
#             print('понедельник')
#             break
#         elif day == days[1]:
#             print('вторник')
#             break
#         elif day == days[2]:
#             print('среда')
#             break
#         elif day == days[3]:
#             print('четверг')
#             break
#         elif day == days[4]:
#             print('пятница')
#             break
#         elif day == days[5]:
#             print('суббота')
#             break
#         elif day == days[6]:
#             print('воскресенье')
#             break
#         else:
#             print('Такого дня не существует.')
#             break

# show_day_of_week(day = int(input('Введите день недели: ')))

# def show_day(num):
    # week = ['Monday', 'Tuesday', 'Wednesday', 
    #        'Thursday', 'Friday', 'Saturday', 
    #         'Sunday']
#     day = [1, 2, 3, 4, 5, 6, 7]
#     for i in day:
#         1 == 'Monday'
#         2 == 'Tuesday'
#         3 == 'Wensday'
#         4 == 'Thursday'
#         5 == 'Friday'
#         6 == 'Saturday'
#         7 == 'Sunday'
#         if num == day:
#             print('i')
#             break
# #show_day(2)
# show_day(num = int(input('Введите день недели: ')))

# 4 Найти максимальное из трех чисел

# def maxNumbers3(a, b, c):
#     if b < a > c:
#         return f'max {a}'
#     elif a < b > c:
#         return f'max {b}'
#     elif a < c > b:
#         return f'max {c}'
#     else:
#         return 'Числа равны'

# print(maxNumbers3(75, 75, 75))

def max_from_3(i):
    
    list = [3]
    len(list): 2
    while len(list) < 2:
        list = [i]
        return max_from_3(i)
    #len(list) == 2
    for j in list:
        print(j)


max_from_3(i = int(input('Enter nambers: ')))

# 5. Написать программу вычисления значения функции y = f(a)



# 6. Выяснить является ли число чётным

# def eventNumber(a):
#     if a % 2 == 0:
#         return print('Число четное')
#     else:
#         return print('Число нечетное')

# eventNumber(a = int(input('Введите число: ')))

# 7. Показать числа от -N до N

# def show_numbers_from_N_to_N(N):
#     for i in range(-N, N + 1):
#         print(i)

# show_numbers_from_N_to_N(N = int(input('Введите число N: ')))

# 8. Показать четные числа от 1 до N

# a = int(input('Введите число: '))
# for i in range(1, a + 1):
#     if i % 2 == 0:
#         print(i)

# 9. Показать последнюю цифру трёхзначного числа


# 10. Показать вторую цифру трёхзначного числа

# def showNumbers(a):
    
#     b = a // 10 % 10
#     print(b)

# showNumbers(a = int(input('Введите трехзначное число: ')))

# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа


# 12. Удалить вторую цифру трёхзначного числа

# print('Удалить вторую цифру трёхзначного числа.')
# def deleteNumberString(a):
#     for i in a:
#         if i == a[2]:
#             print(f'{a[0]}{a[2]}')
#             break
#         elif i > a[2]:
#             print(f'{a[1]}{a[3]}')
#             break

# deleteNumberString(a = input('Введите трехзначное число: '))

# def deleteNumberMath(b):
#     digit3 = b % 10
#     digit1 = b // 100
#     print(digit1 * 10 + digit3)

# deleteNumberMath(b = int(input('Второй способ. Введите трехзначное число: ')))

# 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.


# 14. Найти третью цифру числа или сообщить, что её нет

# 15. Дано число. Проверить кратно ли оно 7 и 23


# 16. Дано число обозначающее день недели. Выяснить является номер дня недели выходным