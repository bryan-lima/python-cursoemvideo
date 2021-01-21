# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

def vote(birth):
    from datetime import datetime
    age = datetime.now().year - birth
    if age < 16:
        return f'Com {age} anos: NÃO VOTA.'
    elif age < 18 or age >= 65:
        return f'Com {age} anos: VOTO OPCIONAL.'
    else:
        return f'Com {age} anos: VOTO OBRIGATÓRIO.'


print('-' * 30)
yearOfBirth = int(input('Em que anos você nasceu? '))
print(vote(yearOfBirth))
