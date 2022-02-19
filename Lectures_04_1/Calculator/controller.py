# Mодуль для связывания model and view

import model_oper as model
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    operat = view.get_oper()

    model.init(value_a, value_b)
    result = model.do_it(operat)
    view.view_data(result)