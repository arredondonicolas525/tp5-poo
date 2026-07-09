#---------------------------PUNTO 2-----------------------------------

import math
from modelo_elementoGrafico import ElementoGrafico
from modeloPunto import Punto

class Elipse(ElementoGrafico):
    def __init__(self, colorHex: str, posicionCentro: Punto, nombreCapa: str, radioMayor: float, radioMenor: float):

        super().__init__(colorHex, posicionCentro, nombreCapa)
        

        if radioMayor <= 0 or radioMenor <= 0:
            raise ValueError("Los radios deben ser mayores a 0")
        

        self._radioMenor = min(radioMenor, radioMayor)
        self._radioMayor = max(radioMenor, radioMayor)
    

    @property
    def radioMenor(self) -> float:
        return self._radioMenor
    
    @radioMenor.setter
    def radioMenor(self, valor: float):
        if valor <= 0:
            raise ValueError("El radio menor debe ser mayor a 0")
        self._radioMenor = min(valor, self._radioMayor)
        self._radioMayor = max(valor, self._radioMenor)
    
    @property
    def radioMayor(self) -> float:
        return self._radioMayor
    
    @radioMayor.setter
    def radioMayor(self, valor: float):
        if valor <= 0:
            raise ValueError("El radio mayor debe ser mayor a 0")
        self._radioMayor = max(valor, self._radioMenor)
        self._radioMenor = min(valor, self._radioMayor)
    

    def calcularArea(self) -> float:
        """Área de la elipse = π * rMenor * rMayor"""
        return math.pi * self._radioMenor * self._radioMayor
    
    def calcularPerimetro(self) -> float:
        """
        Perímetro de la elipse (fórmula aproximada de Ramanujan):
        P ≈ π * [3(rMayor + rMenor) - sqrt((3rMayor + rMenor)(rMayor + 3rMenor))]
        """
        a = self._radioMayor
        b = self._radioMenor
        h = ((a - b) ** 2) / ((a + b) ** 2)
        perimetro_aproximado = math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))
        return perimetro_aproximado
    
    def escalar(self, factor: float) -> None:
        """
        Multiplica ambos radios por el factor.
        
        Comentario sobre casos especiales (mismo criterio que Rectangulo):
        - factor == 0: La elipse degenera a un punto (área 0)
        - factor < 0: No permitido (lanzaría excepción)
        """
        if factor < 0:
            raise ValueError("El factor de escala no puede ser negativo")
        
        self._radioMenor *= factor
        self._radioMayor *= factor
    
    def __str__(self) -> str:
        """Sobrescribe toString invocando a super()"""
        base_str = super().__str__()
        return (f"{base_str}, Tipo=Elipse, "
                f"radioMenor={self._radioMenor}, radioMayor={self._radioMayor}, "
                f"Area={self.calcularArea():.2f}, Perimetro={self.calcularPerimetro():.2f}")

#---------------------------PUNTO 2-----------------------------------