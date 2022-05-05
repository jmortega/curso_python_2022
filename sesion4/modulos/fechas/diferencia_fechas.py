from datetime import datetime, time

def diferencia_fechas_segundos(dt2, dt1):
    timedelta = dt2 - dt1
    return timedelta.days * 24 * 3600 + timedelta.seconds

def diferencia_fechas(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

#fecha concreta
fecha1 = datetime.strptime('2022-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')

#actual
actual = datetime.now()

print("%d días, %d horas, %d minutos, %d segundos" % diferencia_fechas(diferencia_fechas_segundos(actual, fecha1)))
