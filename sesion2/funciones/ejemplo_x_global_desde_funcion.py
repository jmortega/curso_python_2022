
def funcion2():
    global x
    x = 100
    x = x + 5
    print("La variable x dentro de funcion2 vale: ", x)

def main():
    funcion2()
    global x
    x = x + 10
    print("La variable x dentro de main vale:     ", x)

main()
