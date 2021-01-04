# Desenvolva um programa que leia o primeiro termo e a razão de uma PA
# No final, mostre os 10 primeiros termos dessa progressão

print('=' * 30)
print('{:^30}' .format('10 TERMOS DE UMA PA'))
print('=' * 30)

firstTerm = int(input('\nPrimeiro termo: '))
reason = int(input('Razão: '))
tenthTerm = firstTerm + (10 - 1) * reason

for i in range(firstTerm, tenthTerm + reason, reason):
    print('{}'.format(i), end=' → ')

print('ACABOU')
