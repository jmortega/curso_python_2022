import time

def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Tarea {name}: Computando {total}+{number}')
        sleep()
        total += number
    print(f'Tarea {name}: Suma = {total}')

start = time.time()
tareas = [
    sum("A", [1, 2]),
    sum("B", [1, 2, 3]),
]
end = time.time()
print(f'Time: {end-start:.2f} sec')
