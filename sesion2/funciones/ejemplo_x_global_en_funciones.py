
x = 5
def funcion2():
    global x
    x = x + 5
    print("La variable x dentro de funcion2 vale: ", x)

def main():
    global x
    x = x + 10
    funcion2()
    print("La variable x dentro de main vale:     ", x)

main()
