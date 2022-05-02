
'''El método para actualizar un diccionarrio update() actualiza el diccionario con 
los elementos de otro objeto del diccionario o un objeto iterable de pares clave / valor. 

El método  update() añade elementos al diccionario si la clave no está en el diccionario.
Si la clave está en un diccionario, la actualiza con un nuevo valor.'''

# Crreando un diccionario
diccionario = {'Python': 200, 'Java':150, 'JavaScript':1000,'PHP':50}  
print("Diccionario:",diccionario)  
# Actualizar  
diccionario.update({'Python':500})  
print("Diccionario actualizado:",diccionario)  
diccionario.update({'Java':100,'PHP':100})  
print("Diccionario actualizado:",diccionario)
#añadimos un elemento que no teníamos
diccionario.update({'Go':200})  
print("Diccionario actualizado:",diccionario)    

