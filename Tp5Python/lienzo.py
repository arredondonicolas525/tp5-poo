"""
PUNTO 4 - Clase Lienzo (Canvas)
Representa el contenedor de todos los elementos gráficos.
"""
from modelo_elementoGrafico import ElementoGrafico

class Lienzo:
    def __init__(self):
        self._elementos = []

    def agregar(self, elemento: ElementoGrafico) -> None:
        self._elementos.append(elemento)

    @property
    def elementos(self):
        return self._elementos

    def __len__(self):
        return len(self._elementos)

    def __str__(self):
        return f"Lienzo con {len(self)} elementos"