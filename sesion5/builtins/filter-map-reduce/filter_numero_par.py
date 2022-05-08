def esPar(num):
    if num%2 == 0:
        return True
    else:
        return False
    
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter sobre función
print(list(filter(esPar, data)))
