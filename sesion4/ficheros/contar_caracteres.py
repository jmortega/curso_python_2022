import os.path

if os.path.isfile(r"fichero.txt"):
    f = open(r"fichero.txt", "r")
    contador = 0
    linea = f.readline()
    while(linea != ''):
        for caracter in linea:
            if ((caracter != ' ') and (caracter != '\n')):
                contador += 1
        linea = f.readline()
    print("El total de caracteres del fichero es:", contador)
    f.close()
else:
    print("El fichero que estás queriendo leer no existe.")
