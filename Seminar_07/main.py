import controller

select = input('Вычисление комплексных/рациональных чисел (нажмите "1"/"2"):')

if select == '1': 
    controller.calc_complex()
if select == '2': 
    controller.calc_fractional()
