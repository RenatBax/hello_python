import ui
import complex_calc
import float_calc
import login


def calc_complex():
    number_1 = ui.input_data(complex)
    number_2 = ui.input_data(complex)
    oper = ui.input_data(str)    
    result = complex_calc.calc(number_1, number_2, oper)
    login.log_in_file(number_1, number_2, oper, result)
    ui.output_data(result)

def calc_fractional():
    number_1 = ui.input_data(float)
    number_2 = ui.input_data(float)
    oper = ui.input_data(str)
    result = float_calc.calc(number_1, number_2, oper)
    login.log_in_file(number_1, number_2, oper, result)
    ui.output_data(result)
