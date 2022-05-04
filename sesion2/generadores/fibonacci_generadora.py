def fibonacci():
    a,b = 0,1
    while True:
        yield b
        a,b = b, a+b


fib=fibonacci()

for i in range(10):
    print("Fibonacci",i,":",next(fib))
