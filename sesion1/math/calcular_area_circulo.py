from math import pi
from sys import stderr


def area_circulo(radio):
    return pi * radio ** 2

try:
    r = float(input('Dame el radio de la circunferencia: '))

    print('El area de una circunferencia de radio {0} es {1}.'.format(r, area_circulo(r)))
except ValueError as e:
    print('El valor introducido no es un número real', file=stderr)