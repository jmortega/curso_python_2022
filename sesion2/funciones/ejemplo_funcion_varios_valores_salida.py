
def calculo_multiple(a, b):
    sum = a + b
    res = a - b
    mul = a * b
    return(sum, res, mul, a / b, a ** b)

def main():
    print("Introduce los dos valores sobre los que se harán los cálculos:")
    num1 = eval(input("número 1: "))
    num2 = eval(input("número 2: "))
    suma, resta, multiplicacion, division, potencia = calculo_multiple(num1,num2)

    print("La suma es:            ", suma)
    print("La resta es:           ", resta)
    print("La multiplicación  es: ", multiplicacion)
    print("La división es:        ", division)
    print("La potencia es:        ", potencia)

main()
