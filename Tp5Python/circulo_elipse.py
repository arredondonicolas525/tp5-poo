
from modelo_elipse import Elipse
from modeloPunto import Punto
import math

class Circulo(Elipse):
    def __init__(self, colorHex: str, posicionCentro: Punto, nombreCapa: str, radio: float):
        """
        Constructor de Círculo.
        Llama a super() pasando radio como radioMayor y radioMenor (ambos iguales).
        """
        # Ambos radios deben ser iguales (el círculo es una elipse con radios iguales)
        super().__init__(colorHex, posicionCentro, nombreCapa, radio, radio)
        self._radio = radio  # Atributo adicional para claridad
    
    @property
    def radio(self) -> float:
        return self._radio
    
    @radio.setter
    def radio(self, valor: float):
        if valor <= 0:
            raise ValueError("El radio debe ser mayor a 0")
        self._radio = valor
        self._radioMenor = valor
        self._radioMayor = valor
    
    # Sobrescritura de los setters heredados para mantener la integridad
    @Elipse.radioMenor.setter
    def radioMenor(self, valor: float):
        """
        Si se intenta cambiar solo el radio menor, se actualizan ambos radios
        para mantener el círculo.
        """
        if valor <= 0:
            raise ValueError("El radio debe ser mayor a 0")
        self._radio = valor
        self._radioMenor = valor
        self._radioMayor = valor
    
    @Elipse.radioMayor.setter
    def radioMayor(self, valor: float):
        """
        Si se intenta cambiar solo el radio mayor, se actualizan ambos radios
        para mantener el círculo.
        """
        if valor <= 0:
            raise ValueError("El radio debe ser mayor a 0")
        self._radio = valor
        self._radioMenor = valor
        self._radioMayor = valor
    
    def escalar(self, factor: float) -> None:
        """Escala el círculo manteniendo la proporción."""
        if factor < 0:
            raise ValueError("El factor de escala no puede ser negativo")
        self._radio *= factor
        self._radioMenor = self._radio
        self._radioMayor = self._radio
    
    def calcularArea(self) -> float:
        """Área del círculo = π * r²"""
        return math.pi * self._radio ** 2
    
    def calcularPerimetro(self) -> float:
        """Perímetro del círculo = 2 * π * r"""
        return 2 * math.pi * self._radio
    
    def __str__(self) -> str:
        """Sobrescribe toString invocando a super() y agregando información específica"""
        base_str = super().__str__()
        return f"{base_str}, Tipo=Círculo, radio={self._radio}"