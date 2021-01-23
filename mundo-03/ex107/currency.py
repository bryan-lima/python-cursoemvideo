def increase(value, rate):
    increased = value + (value * rate / 100)
    return increased


def decrease(value, rate):
    decreased = value - (value * rate / 100)
    return decreased


def double(value):
    doubled = value * 2
    return doubled


def half(value):
    halved = value / 2
    return halved
