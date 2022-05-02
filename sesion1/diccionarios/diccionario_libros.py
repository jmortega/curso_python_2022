libro: dict = dict({
    'titulo': 'Curso de python',
    'isbn': '1111111',
    'autores': ['autor1'],
    'año': 2021
})

print(libro.items())

print(f"- Titulo {libro.get('titulo')}")
print(f"- isbn {libro.get('isbn')}")
print(f"- autores {libro.get('autores')}")
print(f"- año {libro.get('año')}")

libro: dict = dict({
    'titulo': 'Curso de python actualizado',
    'isbn': '2222222',
    'autores': ['autor1','autor2'],
    'año': 2022
})

print(libro.keys())
print(libro.values())

