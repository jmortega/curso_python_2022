import datetime
print("El dia y la hora de hoy es: ", datetime.datetime.now())
print("El dia de hoy es: ", datetime.date.today())

fecha = datetime.datetime(2022,1,1,00,00,00,1)
print(fecha)
print("Año: ",fecha.year)
print("Mes: ",fecha.month)
print("Día: ",fecha.day)
print("Hora: ",fecha.hour)
print("Minutos: ",fecha.minute)
print("Segundos: ",fecha.second)
print("Microsegundos: ",fecha.microsecond)

print("Diferencia entre 2 fechas:")
print("1.- ", datetime.datetime.now())
print("2.- ", fecha)
resultado = datetime.datetime.now() - fecha
print("Resultado: ",resultado)
