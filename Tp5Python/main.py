"""
PUNTO 4 - Motor de Renderizado y Polimorfismo
Este script:
- Crea varias figuras (Rectángulo, Elipse, Cuadrado, Círculo).
- Las agrega a un Lienzo.
- Aplica filtro de grises y movimiento a todas.
- Intenta sumar áreas (lo cual falla) para demostrar el problema.
"""

from modeloPunto import Punto
from modelo_rectangulo import Rectangulo
from modelo_elipse import Elipse
from cuadrado_rectangulo import Cuadrado
from circulo_elipse import Circulo
from lienzo import Lienzo

def main():
    # 1. Instanciar varias figuras
    figuras = [
        Rectangulo("#FF0000", Punto(10, 20), "capa1", 4, 8),
        Rectangulo("#00FF00", Punto(30, 40), "capa2", 5, 5),
        Elipse("#0000FF", Punto(50, 60), "capa3", 6, 3),
        Cuadrado("#FFFF00", Punto(70, 80), "capa4", 7),
        Circulo("#FF00FF", Punto(90, 100), "capa5", 5),
        Elipse("#AA00AA", Punto(110, 120), "capa6", 4, 2)
    ]

    # 2. Crear el lienzo y agregar figuras
    lienzo = Lienzo()
    for fig in figuras:
        lienzo.agregar(fig)

    print("=== ANTES DEL FILTRO ===")
    for elem in lienzo.elementos:
        print(elem)

    # 3. Bucle: cambiar color a gris y mover a (0,0)
    print("\n=== APLICANDO FILTRO Y MOVIMIENTO ===")
    area_total = 0.0

    for elemento in lienzo.elementos:
        # Cambiar color a gris
        elemento.colorHex = "#808080"
        # Mover al punto (0,0)
        elemento.moverA(Punto(0, 0))

        # INTENTAR SUMAR ÁREAS - ESTO FALLA (descomentar para ver el error)
        area_total += elemento.calcularArea()

        # Mostramos progreso
        print(f"Procesado: {type(elemento).__name__} - Color: {elemento.colorHex} - Posición: {elemento.posicionCentro}")

    print("\n=== DESPUÉS DEL FILTRO ===")
    for elem in lienzo.elementos:
        print(elem)

    # Explicación del error
    print("\n--- ANÁLISIS DEL ERROR ---")
    print("Si descomentamos 'area_total += elemento.calcularArea()', obtenemos:")
    print("AttributeError: 'ElementoGrafico' object has no attribute 'calcularArea'")
    print("Motivo: aunque las subclases tienen el método, ElementoGrafico NO lo define.")
    print("Al tratar a todas como ElementoGrafico, Python busca el método en esa clase.")
    print("Solución: hacer abstracta la clase base y declarar el método allí (Punto 5).")
    
    print(f"\nÁrea total de todas las figuras: {area_total:.2f}")
if __name__ == "__main__":
    main()
    