# Переменное число параметров
# def total(initial=5, *numbers, **keywords):
#     count = initial
#     for number in numbers:
#         count += number
#     for key in keywords:
#         count += keywords[key]
#     return count

# print(total(10, 1, 2, 3, vegetables=50, fruits=100))

# Ключевые параметры
# Объявление параметров после параметра со звёздочкой даёт только ключевые аргументы

# def total(initial=5, *numbers, extra_number): #  def total(initial=5, *, extra_number).
#     count = initial
#     for number in numbers:
#         count += number
#     count += extra_number
#     print(count)

# total(10, 1, 2, 3, extra_number=50)
# # total(10, 1, 2, 3) # Вызовет ошибку, поскольку мы не указали значение
# # аргумента по умолчанию для 'extra_number'.

def someFunction():
    pass
print(someFunction())

def printMax(x, y):
    '''Выводит максимальное из двух чисел. 
        
        Оба значения должны быть целыми числами.''' 
        # строка документации для этой функции
    x = int(x) # конвертируем в целые, если возможно
    y = int(y)
    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')
printMax(3, 5)
print(printMax.__doc__)
