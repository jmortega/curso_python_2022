# Función con Parámetros No Tipados
def miFuncionConParametros(a,b):
    print(f"¡{a}, {b}!")

miFuncionConParametros('Hola', 'Mundo')

# Función con Parámetros Tipados
def miFuncionConParametrosTipados(a: str, b: str) :
    print(f"¡{a}, {b}!")

miFuncionConParametrosTipados('Hola', 'Mundo')

# Función con parámetros por defecto
def miFuncionConParametrosPorDefecto(a, b = 1) :
    print(f"La división es {a/b}")

# llamando la función y pasándole los dos parámetros
miFuncionConParametrosPorDefecto(3, 4)
# llamando la función y pasándole un único parámetro
miFuncionConParametrosPorDefecto(3)

# Función con multiples parámetros
def miFuncionConMultiplesParametros(*elementos) :
    for elemento in elementos:
        print(f"Elemento: {elemento}")

# llamando la función y pasándole una lista de parámetros
lista: [int] = [1, 2, 3, 4, 5]
miFuncionConMultiplesParametros(lista)

# Función con Retorno
def miFuncionConRetorno() -> str:
    return '¡Hola, Mundo!'

hola_mundo = miFuncionConRetorno()
print(hola_mundo)

# Función con Retorno Tipado
def miFuncionConRetornoTipado(elementos) -> int :
    # Inicializamos la variable suma a 0 para incrementarla después
    suma: int = 0

    # iteramos sobre los elementos y los vamos sumando uno a uno
    # los guardamos en la variable suma que se va incrementando
    for elemento in elementos:
        print(f"Elemento: {elemento}")
        suma += elemento

    return suma

lista_numeros = [1, 2, 3, 4, 5, 6]
sumatorio = miFuncionConRetornoTipado(lista_numeros)
print(f"EL sumatorio total es: {sumatorio}")

# Pasando Diccionarios por parámetro
def miFuncionConParametroDiccionario(**numeros) -> int:
    print (numeros) # {'number1' : 10, 'number2' : 20}
    return (numeros['number1'] + numeros['number2'])

# llamando la función y pasándole una diccionario como parámetros
miSuma = miFuncionConParametroDiccionario(number1=10, number2=20)
print(f"{miSuma} es el total")

