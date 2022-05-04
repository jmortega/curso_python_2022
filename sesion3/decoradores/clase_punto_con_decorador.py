class Punto:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        self._x = valor

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, valor):
        self._y = valor


if __name__ == '__main__':
    p1 = Punto(1, 2)
    print(p1.x, p1.y)
    p1.x = 5
    p1.y = 8
    print(p1.x, p1.y)
