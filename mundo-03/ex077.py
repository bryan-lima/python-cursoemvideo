# Crie um programa que tenha uma tupla com várias palavras (não usar acentos)
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

tupleOfWords = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
                'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for word in tupleOfWords:
    print(f'\nNa palavra {word.upper()} temos ', end='')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
