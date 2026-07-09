
from modelo_rectangulo import Rectangulo
from modeloPunto import Punto

class Cuadrado(Rectangulo):
    def __init__(self, colorHex: str, posicionCentro: Punto, nombreCapa: str, lado: float):
        """
        Constructor de Cuadrado.
        Llama a super() pasando lado como ladoMenor y ladoMayor (ambos iguales).
        """
        super().__init__(colorHex, posicionCentro, nombreCapa, lado, lado)
        self._lado = lado
    
    @property
    def lado(self) -> float:
        return self._lado
    
    @lado.setter
    def lado(self, valor: float):
        if valor <= 0:
            raise ValueError("El lado debe ser mayor a 0")
        self._lado = valor
        self._ladoMenor = valor
        self._ladoMayor = valor
    
    # Sobrescritura de los setters heredados para mantener la integridad
    @Rectangulo.ladoMenor.setter
    def ladoMenor(self, valor: float):
        """
        Si se intenta cambiar solo el lado menor, se actualizan ambos lados
        para mantener el cuadrado.
        """
        if valor <= 0:
            raise ValueError("El lado debe ser mayor a 0")
        self._lado = valor
        self._ladoMenor = valor
        self._ladoMayor = valor
    
    @Rectangulo.ladoMayor.setter
    def ladoMayor(self, valor: float):
        """
        Si se intenta cambiar solo el lado mayor, se actualizan ambos lados
        para mantener el cuadrado.
        """
        if valor <= 0:
            raise ValueError("El lado debe ser mayor a 0")
        self._lado = valor
        self._ladoMenor = valor
        self._ladoMayor = valor
    
    def escalar(self, factor: float) -> None:
        """Escala el cuadrado manteniendo la proporción."""
        if factor < 0:
            raise ValueError("El factor de escala no puede ser negativo")
        self._lado *= factor
        self._ladoMenor = self._lado
        self._ladoMayor = self._lado
    
    def __str__(self) -> str:
        """Sobrescribe toString invocando a super() y agregando información específica"""
        base_str = super().__str__()
        return f"{base_str}, Tipo=Cuadrado, lado={self._lado}"