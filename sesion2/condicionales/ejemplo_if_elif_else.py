def main():
    numero = eval(input("Introduce un número: "))
    if numero > 0:
        print("El número es mayor que cero")
    elif numero == 0:
        print("El número es cero.")
    else:
        print("El número es menor que cero")

if __name__ == '__main__':
    main()
