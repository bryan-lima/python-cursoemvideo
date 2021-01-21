# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável

def write(msg):
    tilde = len(msg) + 4
    print('~' * tilde)
    print(f'  {msg}')
    print('~' * tilde)


write('Bryan Lima')
write('Curso de Python no Youtube')
write('CeV')
print()
write(str(input('Digite um texto: ')))
