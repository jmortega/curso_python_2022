import asyncio

async def factorial(n):
    f = 1
    for i in range(2, n + 1):
        print(f"Calculando factorial({n}), actualizando i={i}...")
        await asyncio.sleep(1)
        f *= i
    return f

async def main():
    lista = await asyncio.gather(factorial(2), factorial(3), 
    factorial(4), factorial(5), factorial(6))
    print(lista)

asyncio.run(main())
