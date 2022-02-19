
def input_data(input_type):
    choose_method = 0
    if input_type is complex:
        choose_method = 1
        input_info = 'Complex number: '
    elif input_type is float:
        choose_method = 2
        input_info = 'Fraction number: '
    else:
        choose_method = 0
        input_info = 'Operation (+-/*): '
    call = {
        0: check_oper,
        1: check_complex,
        2: check_fraction,
    }

    while True:
        try:
            data = input(input_info)
            return call[choose_method](data)
        except Exception:
            print(Exception.args)
            continue

def check_complex(input):
    return complex(input)

def check_oper(input):
    if input in ['-','+','*','/']:
        return str(input)    
    else:
        return None

def check_fraction(input):
    return float(input)

def output_data(result):
    if type(result) == float:
        print(f'{result:.2f}')
    else:
        print(result)
