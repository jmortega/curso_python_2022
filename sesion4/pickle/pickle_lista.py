import pickle
lista = ['test value','test value 2','test value 3']
fichero = "fichero.pickle"
# abrir el fichero para escritura
fileObject = open(fichero,'wb') 
# escribir el objeto lista en el fichero
pickle.dump(lista,fileObject)   
# cerrar el descriptor de fichero
fileObject.close()
# abrir el fichero para lectura
fileObject = open(fichero,'rb')  
# cargar el objeto desde el fichero y guardarlo en una variable lista2
lista2 = pickle.load(fileObject)
print(lista2)
print(lista==lista2)
