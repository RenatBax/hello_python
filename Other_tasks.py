# Задача 1
# Подсчитать количество натуральных чисел, не превосходящих заданного числа n, которые
        # делятся на k, но не на l
        # делятся хотябы на k или на l
        # не делятся на (k + l)

# def natural_numbers_not_exceeding_given_number(k = 7, l = 4):
    
#     for i in range(1, 100):
#         if i % k == 0 and not i % l:
#             print(f'\\{i}\\', end=' ')
#     print()
#     for i in range(1, 100):
#         if i % k == 0 or i % l == 0:
#             print(f'\"{i}\"', end=' ')
#     print()
#     for i in range(1, 100):
#         if not i % (k + l):
#             print(f'\'{i}\'', end=' ')

# natural_numbers_not_exceeding_given_number()

# Задача 2
# Задать положительное вещественное число m. Cоставить целое число n из цифр
        # десятков и сотых m
        # единиц и сотых m
        # сотен и десятых m

def make_an_integer(real_numb):
    str_numb = str(real_numb)
    clear_numb = str_numb.replace('.', '')
    int_10 = int(clear_numb[2:7])
    int_1 = int(clear_numb[3:7])
    int_100 = int(clear_numb[1:6])
    return int_10, int_1, int_100

m = int(input('Введите положительное вещественное число: '))
make_an_integer(m)

# Задача 2
# Написать программу, вычисляющую значение периодической функции f(x), 
# в произвольной точке x, если на промежутке [a;b], который составляет один её период, 
# значения функции вычисляются по формуле
        # - [-3; 3], f(x) = |x| - 1
        # - [-10; -2], f(x) = 1/x + 0.6
        # - [-4; 3], f(x) = Cos(|π*x|)