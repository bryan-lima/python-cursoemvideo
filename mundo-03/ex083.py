# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

# Minha solução inicial, sem usar lista
# from sys import exit
#
# expression = str(input('\nDigite a expressão: ')).strip()
# parentheses = 0
#
# if expression.count('(') == 0 and expression.count(')') == 0:
#     print('Você não utilizou parênteses na expressão digitada')
# elif expression.count('(') == expression.count(')'):
#     for character in expression:
#         if character == '(':
#             parentheses += 1
#         elif character == ')':
#             parentheses -= 1
#
#         if parentheses < 0:
#             print('Sua expressão está errada!')
#             exit(0)
#     print('Sua expressão está válida!')
# elif expression.count('(') != expression.count(')'):
#     print('Sua expressão está errada!')

expression = str(input('\nDigite a expressão: ')).strip()
stack = []

for character in expression:
    if character == '(':
        stack.append('(')
    elif character == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break

if len(stack) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
