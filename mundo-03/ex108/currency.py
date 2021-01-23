def increase(value=0, rate=0):
    increased = value + (value * rate / 100)
    return increased


def decrease(value=0, rate=0):
    decreased = value - (value * rate / 100)
    return decreased


def double(value=0):
    doubled = value * 2
    return doubled


def half(value=0):
    halved = value / 2
    return halved


def currency(value=0, currency='R$'):
    return f'{currency} {value:.2f}'.replace('.', ',')
