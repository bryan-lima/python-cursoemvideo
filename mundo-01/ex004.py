# Documentação oficial sobre os tipos embutidos no Python: https://docs.python.org/pt-br/3/library/stdtypes.html
# Sobre identificador válido, veja mais em: https://docs.python.org/pt-br/3/reference/lexical_analysis.html#identifiers

n = input('Digite algo: ')
print('O tipo primitivo desse valor é: {}' .format(type(n)))
print('É alfanumérico?: {}' .format(n.isalnum()))
print('É alfabético?: {}' .format(n.isalpha()))
print('É um numéro?: {}' .format(n.isnumeric()))
print('Os caracteres são ASCII?: {}' .format(n.isascii()))
print('É decimal?: {}' .format(n.isdecimal()))
print('É dígito?: {}' .format(n.isdigit()))
print('É um identificador válido?: {}' .format(n.isidentifier()))
print('Só tem espaço?: {}' .format(n.isspace()))
print('Está tudo em minúsculo?: {}' .format(n.islower()))
print('Está tudo em MAIÚSCULO?: {}' .format(n.isupper()))
print('Está capitalizado?: {}' .format(n.istitle()))
print('Pode ser impresso?: {}' .format(n.isprintable()))
