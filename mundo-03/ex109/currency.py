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
