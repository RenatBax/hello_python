x = 0
y = 0

def init(a, b): # Метод отвечающий за инициализацию вводимых значений
    global x
    global y
    x = a
    y = b

def do_it(oper):
    if oper == '+':
        return x + y
    if oper == '-':
        return x - y
    if oper == '*':
        return x * y
    if oper == '/':
        return x / y