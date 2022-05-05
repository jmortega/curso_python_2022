import json

data = {}
data['clientes'] = []

data['clientes'].append({
    'nombre': 'Cliente1',
    'apellidos': 'Apellido1',
    'edad': 20,
    'profesion': 'profesion1'})
data['clientes'].append({
    'nombre': 'Cliente2',
    'apellidos': 'Apellido2',
    'edad': 30,
    'profesion': ['profesion1']})
data['clientes'].append({
    'nombre': 'Cliente3',
    'apellidos': 'Apellido3',
    'edad': 40,
    'profesion': ['profesion1','profesion2']})
with open('data.json', 'w') as file:
	json.dump(data, file, indent=4)
