# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado

import urllib
import urllib.request

colors = {
    'clear': '\033[m',
    'txtRedBold': '\033[1:31m',
    'txtGreenBold': '\033[1:32m',
    'txtYellowBold': '\033[1:33m',
}

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print(colors['txtRedBold'] + 'O site Pudim não está acessível no momento.' + colors['clear'])
else:
    print(colors['txtYellowBold'] + 'Consegui acessar o site Pudim com sucesso!' + colors['clear'])
