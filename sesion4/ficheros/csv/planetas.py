import csv
from dataclasses import dataclass

def lectura_csv(nombre_fichero):
	results = []
	with open(nombre_fichero, 'r') as file:
		reader = csv.reader(file)
		for fila in reader:
			results.append(fila)
	return results

def lectura_csv2(nombre_fichero):
	results = []
	with open(nombre_fichero, 'r') as file:
		reader = csv.DictReader(file)
		for fila in reader:
			results.append(fila)
	return results
	
@dataclass
class Planeta:
    nombre: str
    masa: float
    radio: float

    def __post_init__(self):
        self.radio = float(self.radio)
        self.masa = float(self.masa)

    @property
    def gravedad(self):
        g_constante = 6.673e-11
        return g_constante * self.masa / (self.radio ** 2)


def lectura_de_planetas(nombre_fichero):
    with open(nombre_fichero, 'r') as fr:
        reader = csv.reader(fr)
        tiene_cabecera = csv.Sniffer().has_header(fr.read(1024))
        fr.seek(0)  # colocando la posición de lectura al inicio de nuevo
        if tiene_cabecera:
            cabecera = next(reader)  # se ignora la cabecera
        for fila in reader:
            yield Planeta(*fila)


if __name__ == '__main__':
    planetas = lectura_csv('planetas.csv')
    print(planetas)
    for p in lectura_de_planetas('planetas.csv'):
        print(f'La gravedad en {p.nombre} es {p.gravedad}')
