cesta_compra = {"articulo1":1000,"articulo2":3000,"articulo3":3000}

#cesta_compra = {}
#articulo = input('Introduce un artículo: ')
#precio = float(input('Introduce el precio de ' + articulo + ': '))
#cesta_compra[articulo] = precio

print('Lista de la compra')
print(cesta_compra.items())
print(cesta_compra.keys())
print(cesta_compra.values())

coste_total=0

for articulo, precio in cesta_compra.items():
    print(articulo, ':', precio)
    coste_total += precio
    
print('Coste total: ', coste_total)
