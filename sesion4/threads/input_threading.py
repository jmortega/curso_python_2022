import threading
import queue
import time

def otra_funcion():
	time.sleep(5) 
	print("ejecuto otra función mientras espero entrada por teclado")
	
def read_keyboard_input(inputQueue):
    print('Introduce una cadena:')
    while (True):
        input_str = input()

        #Encolamos el input de entrada
        inputQueue.put(input_str)

def main():

    EXIT_COMMAND = "exit"
    inputQueue = queue.Queue()
    
    # Creamos un hilo para leer las entradas del teclado.
    # daemon = True para crear un subproceso de forma automática
    inputThread = threading.Thread(target=read_keyboard_input, args=(inputQueue,), daemon=True)
    inputThread.start()

    # bucle principal
    while (True):
    	otra_funcion()
    	if (inputQueue.qsize() > 0):
    		input_str = inputQueue.get()
    		print("input_str = {}".format(input_str))
    		if (input_str == EXIT_COMMAND):
    			print("Exiting serial terminal.")
    			break
    	# Dormimos el bucle principal durante 1 milisegungo para evitar
    	# que el hilo obtenga todos los recursos de la CPU
    	time.sleep(0.01) 

    print("Fin del bucle principal")

if __name__== '__main__': 
    main()

