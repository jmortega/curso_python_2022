x = [2, 8, 1, 4, 6, 3, 7] 
print(sorted(x))  # Devuelve la lista ordenada
print(sorted(x, reverse = True))  # Devuelve la lista en ordenada en orden inverso

x = {'q':1, 'w':2, 'e':3, 'r':4, 't':5, 'y':6} 
sorted(x) 

Lista = ["cccc", "b", "dd", "aaa"] 
  
print("Ordenacion normal:", sorted(Lista))
print("Ordenacion por longitud:", sorted(Lista, key = len))

def funcion_ordenacion(x): 
    return x%2!=0
 
Lista= [10, 25, 30, 50]  
print("Ordenacion normal:", sorted(Lista))
print("Ordenacion por funcion:", sorted(Lista, key = funcion_ordenacion))




