from collections import Counter

c = Counter("Curso de python")
print(c)
d = Counter({"d": 6, "i": 8})

e = c + d

print(e)
print(c.most_common())
