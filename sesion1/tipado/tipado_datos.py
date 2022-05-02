from typing import Tuple, Dict, List, Set

tupla: Tuple = (0, 1, 2, 3)
diccionario: Dict = {'key': 'value'}
lista: List = [0, 1, 2, 3]
conjunto: Set = {0, 1, 2, 3}

print(tupla)
print(diccionario)
print(lista)
print(conjunto)

def suma(num1: int, num2: int) -> int:
    return num1 + num2
    
print(suma(1,2))
