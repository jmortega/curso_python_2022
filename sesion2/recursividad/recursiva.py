def jugar(intento=1):
    respuesta = input("Lenguaje de programacion favorito ")
    if respuesta != "python":
        if intento < 3:
            print("\nYOU FAIL xD Inténtalo de nuevo")
            intento += 1
            jugar(intento) # Llamada recursiva
        else:
            print("\nPerdiste!")
    else:
        print("\nGanaste!")
jugar()
