# Importa la librería para utilizar SQLite
import sqlite3

# Conecta a la base de datos
database = sqlite3.connect('coches.db')

# Apertuda de un cursor
cursor = database.cursor()

# Lectura de todos los coches
cursor.execute("SELECT * FROM Coche")
print("Mostrando todos los coches:")
for registro in cursor:
    print(registro)

# Lectura de todos los fabricantes
cursor.execute("SELECT * FROM Fabricante")
print("Mostrando todos los fabricantes:")
for registro in cursor:
    print(registro)
    
# Lectura de todos los coches a partir del fabricantes
cursor.execute("SELECT * FROM Fabricante")
for registro in cursor:
    print("Mostrando todos los coches del fabricante: ", registro[1])
    # Nuevo cursor para ejecutar la consulta para los coches
    cursorcoches = database.cursor()
    # Ejecución de la query
    parametro = (registro[0],)
    cursorcoches.execute("SELECT Modelo, Cilindrada, Color FROM Coche where FabricanteId = ?",parametro)
    # Muestra la información de cada coche asociada al fabricante
    for registrocoche in cursorcoches:
        print(registro[1]," ",registrocoche[0],", ",registrocoche[1], "cc, ", registrocoche[2])
        
# Eliminación de un coche
#query = "DELETE FROM Coche WHERE id = 4"
#cursor.execute(query)
#database.commit()

# Cierra la conexión a la base de datos    
database.close()
