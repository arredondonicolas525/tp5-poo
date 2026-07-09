#------------------------PUNTO 1------------------------
class Punto:
    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, valor: float):
        self._x = valor

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, valor: float):
        self._y = valor

    def __str__(self) -> str:
        return f"Punto({self._x}, {self._y})"
#------------------------PUNTO 1------------------------