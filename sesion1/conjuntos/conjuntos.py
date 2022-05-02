a = set([1,2,3,4,5,6,7])
b = frozenset([4,5,6,7]) #inmutable

# Unión
union = a | b 

# Intersección
interseccion = a & b 

# Diferencia
diferencia = a - b 

print("Union",union)
print("Intersección",interseccion)
print("Diferencia",diferencia)

if 4 in a:
    print("4 dentro de A")

if a >= b:
    print("A es superconjunto y B es subconjunto")