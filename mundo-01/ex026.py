# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

phrase = str(input('Digite uma frase: ')).strip()
print('Na frase digitada, a letra "A" aparece {} vezes' .format(phrase.upper().count('A')))
print('A primeira letra "A" aparece na posição {}' .format(phrase.upper().find('A') + 1))
print('A última letra "A" aparece na posição {}' .format(phrase.upper().rfind('A') + 1))
