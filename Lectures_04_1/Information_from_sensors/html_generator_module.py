
from ui_module import temperature_view
from ui_module import preassure_view
from ui_module import wind_speed_view

def create(device = 1):
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '    <p {}> Temperature: {} C</p>\n'\
        .format(style, temperature_view(device))
    html += '    <p {}> Preassure: {} mmHg</p>\n'\
        .format(style, preassure_view(device))
    html += '    <p {}> Wind speed: {} m/s</p>\n'\
        .format(style, wind_speed_view(device))
    html += '   </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)
    return html

def new_create(data, device = 1):
    t, p, w = data
    # t = t * 1.8 + 32
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '    <p {}> Temperature: {} C</p>\n'\
        .format(style, t)
    html += '    <p {}> Preassure: {} mmHg</p>\n'\
        .format(style, p)
    html += '    <p {}> Wind speed: {} m/s</p>\n'\
        .format(style, w)
    html += '   </body>\n</html>'

    with open('new_index.html', 'w') as page:
        page.write(html)
    return data