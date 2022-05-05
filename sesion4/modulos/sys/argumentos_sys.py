import sys
print(type(sys.argv))
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])

for item in sys.argv:
    print(item)
