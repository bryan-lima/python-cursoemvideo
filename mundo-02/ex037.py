# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

colors = {
    'clear': '\033[m',
    'txtRedBold': '\033[1:31m',
}

num = int(input('Digite um número inteiro: '))
print('''\nEscolha umas das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
choice = int(input('\nSua escolha: '))

if choice == 1:
    print('\n{} convertido para BINÁRIO é igual a {}' .format(num, bin(num)[2:]))
elif choice == 2:
    print('\n{} convertido para OCTAL é igual a {}' .format(num, oct(num)[2:]))
elif choice == 3:
    print('\n{} convertido para HEXADECIMAL é igual a {}' .format(num, hex(num)[2:]))
else:
    print('\n{}Opção INVÁLIDA! Tente novamente.{}' .format(colors['txtRedBold'], colors['clear']))
