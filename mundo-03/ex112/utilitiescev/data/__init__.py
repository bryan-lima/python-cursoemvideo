colors = {
    'clear': '\033[m',
    'txtRedNormal': '\033[0:31m',
    'txtRedBold': '\033[1:31m',
}


def readMoney(msg):
    while True:
        value = str(input(msg)).replace(',', '.').strip()
        if value.isnumeric() or '.' in value:
            break
        if value == '' or value.isalnum():
            print(f'{colors["txtRedNormal"]}ERRO: \"{value}\" é um preço inválido!{colors["clear"]}\n')
    return float(value)
