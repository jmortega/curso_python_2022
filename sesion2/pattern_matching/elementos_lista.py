def match_list(lista):
    match lista:
    	case []:
        	print("Lista vacía")
    	case [x]:
        	print(f"Lista de un elemento: {x}")
    	case [x, y]:
        	print(f"Lista con dos elementos: {x} y {y}")
    	case [x, y, z]:
        	print(f"Lista con tres elementos: {x}, {y} y {z}")
    	case [x, y, *tail]:
        	print(f"Lista con más de tres elementos. Los dos primeros son: {x} y {y}")
        case [0, 1, 1, 2, *tail]:
        	print(f"Parece que es la serie de Fibonacci...")


match_list([])
match_list([1])
match_list([1, 2])
match_list([1, 2, 3])
match_list([1, 2, 3, 4, 5])
