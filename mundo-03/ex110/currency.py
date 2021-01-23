def increase(value=0, rate=0, formatted=False):
    increased = value + (value * rate / 100)
    return increased if not formatted else currency(increased)


def decrease(value=0, rate=0, formatted=False):
    decreased = value - (value * rate / 100)
    return decreased if not formatted else currency(decreased)


def double(value=0, formatted=False):
    doubled = value * 2
    return doubled if not formatted else currency(doubled)


def half(value=0, formatted=False):
    halved = value / 2
    return halved if not formatted else currency(halved)


def currency(value=0.0, currency='R$'):
    return f'{currency} {value:.2f}'.replace('.', ',')


def resume(value=0, rate_increase=0, rate_decrease=0):
    print('-' * 32)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 32)
    print(f'{"Preço analisado:":<20} {currency(value)}',)
    print(f'{"Dobro do preço:":<20} {double(value, True)}')
    print(f'{"Metade do preço:":<20} {half(value, True)}')
    print(f'{rate_increase}{"% de aumento:":<{20 - findSizeInt(rate_increase)}} {increase(value, rate_increase, True)}')
    print(f'{rate_decrease}{"% de redução:":<{20 - findSizeInt(rate_decrease)}} {decrease(value, rate_decrease, True)}')
    print('-' * 32)


def findSizeInt(number):
    from math import floor, log10

    number = abs(int(number))
    return 1 if number == 0 else floor(log10(number)) + 1
