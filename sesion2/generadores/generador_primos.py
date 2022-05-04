def gen_primos():
    """ Generador de números primos."""
    
    contador = 1
    lista_primos=[]
               
    # Comienza una secuencia infinita.
    while True:
        es_primo = True
        contador += 1
        if len(lista_primos) > 0:
            for primo in lista_primos: 
                if contador % primo == 0:
                    es_primo = False
                    break
        if es_primo:
            lista_primos.append(contador)
            yield contador
			
generador = gen_primos()
print(generador)

numero_primos=1000
i=0
#generar los n primeros primos
while i<numero_primos:
	i = i +1
	print("Primo "+str(i),next(generador))
