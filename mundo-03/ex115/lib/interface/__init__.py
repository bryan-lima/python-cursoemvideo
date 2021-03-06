colors = {
    'clear': '\033[m',
    'txtRedNormal': '\033[0:31m',
    'txtGreenNormal': '\033[0:32m',
    'txtYellowNormal': '\033[0:33m',
    'txtBlueNormal': '\033[0:34m',
    'txtRedBold': '\033[1:31m',
    'txtGreenBold': '\033[1:32m',
    'txtYellowBold': '\033[1:33m',
    'txtBlueBold': '\033[1:34m',
}


def readInt(msg):
    while True:
        try:
            value = int(input(msg))
        except (TypeError, ValueError):
            print(colors['txtRedBold'] + 'ERRO: Por favor, digite um número inteiro válido.' + colors['clear'])
            continue
        except (KeyboardInterrupt):
            print(colors['txtRedBold'] + '\nUsuário preferiu não digitar esse número.' + colors['clear'])
            return 0
        else:
            return value


def line(size=42):
    return '-' * size


def header(txt, size=42):
    print(line())
    print(txt .center(size))
    print(line())


def menu(lst):
    header('MENU PRINCIPAL')
    counter = 1
    for item in lst:
        print(f'{colors["txtYellowNormal"]}{counter}{colors["clear"]} - {colors["txtBlueNormal"]}{item}{colors["clear"]}')
        counter += 1
    print(line())
    option = readInt(f'{colors["txtYellowNormal"]}Sua opção:{colors["clear"]} ')
    return option
