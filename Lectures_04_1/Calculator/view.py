# Модуль для взаимодействия с пользователем

def view_data(data):
    print(f'result = {data}')

def get_value():
    return int(input('number = '))

def get_oper():
    print('Get operations of numbers: +, -, *, /')
    return input()
