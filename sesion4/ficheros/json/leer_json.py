import json

with open('data.json') as file:
    data = json.load(file)
    for cliente in data['clientes']:
        print('Nombre:', cliente['nombre'])
        print('apellidos:', cliente['apellidos'])
        print('Edad:', cliente['edad'])
        print('Profesion:', cliente['profesion'])
