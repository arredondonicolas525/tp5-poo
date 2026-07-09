#------------------------INICIO PUNTO 1------------------------
from abc import ABC, abstractmethod  # <--- NUEVO (Punto 5)
from modeloPunto import Punto

class ElementoGrafico(ABC):  # <--- MODIFICADO (ahora hereda de ABC)
    def __init__(self, colorHex: str = "#000000", posicionCentro: Punto = None, nombreCapa: str = "capa0"):
        self._colorHex = colorHex
        self._posicionCentro = posicionCentro if posicionCentro is not None else Punto(0, 0)
        self._nombreCapa = nombreCapa

    @classmethod
    def con_color_y_posicion(cls, colorHex: str, x: float, y: float, nombreCapa: str = "capa0"):
        return cls(colorHex, Punto(x, y), nombreCapa)

    @property
    def colorHex(self) -> str:
        return self._colorHex

    @colorHex.setter
    def colorHex(self, valor: str):
        self._colorHex = valor

    @property
    def posicionCentro(self) -> Punto:
        return self._posicionCentro

    @posicionCentro.setter
    def posicionCentro(self, nuevo: Punto):
        self._posicionCentro = nuevo

    @property
    def nombreCapa(self) -> str:
        return self._nombreCapa

    @nombreCapa.setter
    def nombreCapa(self, valor: str):
        self._nombreCapa = valor

    def moverA(self, nuevoDestino: Punto) -> None:
        """Actualiza las coordenadas del centro."""
        self._posicionCentro = nuevoDestino

    # -------------------- PUNTO 5 (AGREGADO) --------------------
    @abstractmethod
    def calcularArea(self) -> float:
        """Calcula el área de la figura. Debe ser implementado por las subclases."""
        pass

    @abstractmethod
    def calcularPerimetro(self) -> float:
        """Calcula el perímetro de la figura. Debe ser implementado por las subclases."""
        pass
    # -------------------- FIN PUNTO 5 --------------------

    def __str__(self) -> str:
        return (f"ElementoGrafico[colorHex={self._colorHex}, "
                f"centro={self._posicionCentro}, capa={self._nombreCapa}]")
#------------------------FIN PUNTO 1------------------------
