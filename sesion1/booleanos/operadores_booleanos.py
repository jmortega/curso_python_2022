
verdadero = True
falso = False
print("Valor de la variable verdadero:",verdadero)
print("Valor de la variable falso:",falso)

#Booleanos AND
print("Resultado de True AND True:", True and True)
print("Resultado de True AND False:", True and False)
print("Resultado de False AND True:", False and True)
print("Resultado de False AND False:", False and False)

#Booleanos OR
print("Resultado de True OR True:", True or True)
print("Resultado de True OR False:", True or False)
print("Resultado de False OR True:", False or True)
print("Resultado de False OR False:", False or False)

#Booleanos NOT
print("Resultado de NOT True:", not True)
print("Resultado de NOT False:", not False)

#operaciones
booleano1 = bool(input("Primer valor:"))
booleano2 = bool(input("Segundo valor:"))
booleano3 = bool(input("Tercer valor:"))
booleano4 = bool(input("Cuarto valor:"))
booleano5 = bool(input("Quinto valor:"))
print("Resultado:", booleano4 or ((booleano3 and not booleano2) and booleano1) or booleano5)

#relacionales
numero1 = float(input("Primer número:"))
numero2 = float(input("Segundo número:"))
numero3 = float(input("Tercer número:"))
numero4 = float(input("Cuarto número:"))
print(numero1,"==",numero4,":",numero1==numero4)
print(numero2,"!=",numero3,":",numero2!=numero3)
print(numero3,">",numero2,":",numero3>numero2)
print(numero4,"<",numero1,":",numero4<numero1)
print(numero1,">=",numero3,":",numero1>=numero3)
print(numero2,"<=",numero4,":",numero2<=numero4)




