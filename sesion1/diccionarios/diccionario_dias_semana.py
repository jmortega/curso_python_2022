diassemanaingles = {"Lunes" : "Monday",
                   "Martes" : "Tuesday",
                   "Miercoles" : "Wednesday",
                   "Jueves" : "Thursday",
                   "Viernes" : "Friday"}
print(diassemanaingles["Lunes"])
print(diassemanaingles["Miercoles"])
print(diassemanaingles["Viernes"])

#añadir elementos al diccionario
diassemanaingles["Sabado"] = "Saturday"
print(diassemanaingles)
diassemanaingles["Domingo"] = "Sunday"
print(diassemanaingles)

#funciones sobre el diccionario
print("Número de elementos del diccionario: ",len(diassemanaingles))
print("Elemento mayor del diccionario: ",max(diassemanaingles))
print("Elemento menor del diccionario: ",min(diassemanaingles))

