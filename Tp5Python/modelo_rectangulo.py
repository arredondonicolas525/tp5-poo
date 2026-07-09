#---------------------------PUNTO 2-----------------------------------
from modelo_elementoGrafico import ElementoGrafico
from modeloPunto import Punto

class Rectangulo(ElementoGrafico):
    def __init__(self, colorHex: str, posicionCentro: Punto, nombreCapa: str, ladoMenor: float, ladoMayor: float):
        super().__init__(colorHex, posicionCentro, nombreCapa)
        
        self._ladoMenor = min(ladoMenor, ladoMayor)
        self._ladoMayor = max(ladoMenor, ladoMayor)

        if ladoMenor <= 0 or ladoMayor <= 0:
            raise ValueError("Los lados deben ser mayores a 0")
        

    
    @property
    def ladoMenor(self) -> float:
        return self._ladoMenor
    
    @ladoMenor.setter
    def ladoMenor(self, valor: float):
        if valor <= 0:
            raise ValueError("El lado menor debe ser mayor a 0")
        self._ladoMenor = min(valor, self._ladoMayor)
        self._ladoMayor = max(valor, self._ladoMayor)
    
    @property
    def ladoMayor(self) -> float:
        return self._ladoMayor
    
    @ladoMayor.setter
    def ladoMayor(self, valor: float):
        if valor <= 0:
            raise ValueError("El lado mayor debe ser mayor a 0")
        self._ladoMayor = max(valor, self._ladoMenor)
        self._ladoMenor = min(valor, self._ladoMenor)
    
    # Métodos requeridos
    def calcularArea(self) -> float:
        """Área del rectángulo = ladoMenor * ladoMayor"""
        return self._ladoMenor * self._ladoMayor
    
    def calcularPerimetro(self) -> float:
        """Perímetro del rectángulo = 2 * (ladoMenor + ladoMayor)"""
        return 2 * (self._ladoMenor + self._ladoMayor)
    
    def escalar(self, factor: float) -> None:
        """
        Casos especiales:
         - Si factor == 0: El rectángulo desaparecería (área y perímetro 0).
           En un motor real, quizás se debería eliminar o dejar área 0 pero visible.
         - Si factor < 0: Generaría lados negativos, lo cual no tiene sentido físico.
           Podría interpretarse como una reflexión (espejado) pero manteniendo
           el valor absoluto para el tamaño.
         
         En esta implementación:
         - factor == 0  -> Se mantiene, pero área 0
         - factor < 0   -> Se lanza excepción (no permitido)
        """
        if factor < 0:
            raise ValueError("El factor de escala no puede ser negativo")
        
        self._ladoMenor *= factor
        self._ladoMayor *= factor
        
        # Si factor es 0, ambos lados quedan en 0 
    
    def __str__(self) -> str:
        """Sobrescribe toString invocando a super()"""
        base_str = super().__str__()
        return (f"{base_str}, Tipo=Rectangulo, "
                f"ladoMenor={self._ladoMenor}, ladoMayor={self._ladoMayor}, "
                f"Area={self.calcularArea()}, Perimetro={self.calcularPerimetro()}")

#---------------------------PUNTO 2-----------------------------------