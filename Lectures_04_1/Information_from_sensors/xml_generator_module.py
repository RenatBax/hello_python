# Формат xml - необходим для передачи данных от сервера к клиенту и наоборот. Так же  формат json
from ui_module import temperature_view
from ui_module import preassure_view
from ui_module import wind_speed_view

def create(device = 1):
    xml = '<xml>\n'
    xml += '    <temperature units = "c">{}</temperature>\n'\
        .format(temperature_view(device))
    xml += '    <preassure units = "mmHg">{}</preassure>\n'\
        .format(preassure_view(device))
    xml += '    <wind speed units = "m/s">{}</wind speed>\n'\
        .format(wind_speed_view(device))
    xml += '</xml>'

    with open('data.xml', 'w') as page:
        page.write(xml)
    return xml

def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    w = (w / 1000) * 0.62
    xml = '<xml>\n'
    xml += '    <temperature units = "f">{}</temperature>\n'\
        .format(t)
    xml += '    <preassure units = "mmHg">{}</preassure>\n'\
        .format(p)
    xml += '    <wind speed units = "ml/s">{}</wind speed>\n'\
        .format(w)
    xml += '</xml>'

    with open('new_data.xml', 'w') as page:
        page.write(xml)
    return data