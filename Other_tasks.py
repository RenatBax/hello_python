# Задача 1
# Подсчитать количество натуральных чисел, не превосходящих заданного числа n, которые
        # делятся на k, но не на l
        # делятся хотябы на k или на l
        # не делятся на (k + l)

def natural_numbers_not_exceeding_given_number(k = 7, l = 4):
    
    for i in range(1, 100):
        if i % k == 0 and not i % l:
            print(f'\\{i}\\', end=' ')
    print()
    for i in range(1, 100):
        if i % k == 0 or i % l == 0:
            print(f'\"{i}\"', end=' ')
    print()
    for i in range(1, 100):
        if not i % (k + l):
            print(f'\'{i}\'', end=' ')

natural_numbers_not_exceeding_given_number()

# Задача 2
# Задать положительное вещественное число m. Cоставить целое число n из цифр
        # десятков и сотых m
        # единиц и сотых m
        # сотен и десятых m

def make_an_integer(кeal_numb = 122.954):


