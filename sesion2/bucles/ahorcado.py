# Preguntamos al usuario la palabra a adivinar.
palabra = input('Introduce la palabra a adivinar: ')
# Creamos una lista con los caracteres de la palabra.
palabra = list(palabra)
# Creamos una lista con asteriscos de la misma longitud que la palabra.
solucion = list('*' * len(palabra))
# Inicializamos un contador con los fallos.
fallos = 0
# Mientras quede alguna palabra por adivinar y el numero de fallos sea menor que 5.
while any(palabra) and fallos < 5:
	# Preguntamos al usuario por una letra.
	letra = input('Introduce una letra: ')
	if letra in palabra: # Si la letra esta en la lista con los caracteres de la palabra.
		print('Acierto')
		# Guardamos la posicion de la lista en la que aparece el caracter.
		for letra2 in palabra:
			if(letra2 == letra):
				#posiciones[letra]= palabra.index(letra)
				i = palabra.index(letra2)
				# Cambiamos el caracter por False en esa posicion de la lista de caracteres de la palabra.
				palabra[i] = False
				# Cambiamos el asterisco por el caracter en esa posicion de las lista que contienen la solucion. 
				solucion[i] = letra
	else: # Si la letra no esta en la lista con los caracteres de la palabra.
		print('Fallo')
		# Incrementamos en 1 el contador de fallos.
		fallos += 1
	# Mostramos por pantalla la solucion despues del intento.
	print(solucion)
if fallos == 5: # Si el numero de fallos es 5 hemos perdido.
	print('Perdiste')
else: # Si el numero de fallos es distinto de 5 hemos ganado.
	print('Ganaste')