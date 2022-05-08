a = [1, 2, 3]
b = ["Uno", "Dos", "Tres"]
c = zip(a, b)

print(list(c))
# [(1, 'Uno'), (2, 'Dos'), (3, 'Tres')]

#Es útil combinada con un for para iterar dos listas en paralelo

for numero, texto in zip(a, b):
    print("Número", numero, "Letra", texto)
 
# Número 1 Letra Uno
# Número 2 Letra Dos
# Número 3 Letra Tres
   
numbers = [1, 2]
spanish = ["Uno", "Dos"]
english = ["One", "Two"]
c = zip(numbers, spanish, english)
print(c)

for number, esp, eng  in zip(numbers, spanish, english):
    print(number, esp, eng)
    
# 1 Uno One
# 2 Dos Two

numbers = [1, 2, 3, 4, 5]
for number, esp, eng in zip(numbers, spanish, english):
    print(number,esp,eng)

# 1 Uno One
# 2 Dos Two


spanish = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
english = {'1': 'One', '2': 'Two', '3': 'Three'}

for a, b in zip(spanish, english):
    print(a, b)

# 1 1
# 2 2
# 3 3

for (k1, v1), (k2, v2) in zip(spanish.items(), english.items()):
    print(k1, v1, v2)

#1 Uno One
#2 Dos Two
#3 Tres Three


#unpacking con el *
c = [(1, 'One'), (2, 'Two'), (3, 'Three')]
a, b = zip(*c)

print(a)  # (1, 2, 3)
print(b)  # ('One', 'Two', 'Three')
    





