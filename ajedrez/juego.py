from juegos.piezas.pieza import Pieza
from juegos.piezas.coordenada import Coordenada

# Subclase de Pieza para el juego de Ajedrez
class PiezaAjedrez(Pieza):
    def __init__(self, color, coordenada):
        # En ajedrez, las coordenadas son notación de columnas (A-H) y filas (1-8)
        super().__init__(color, coordenada)

# Crear algunas piezas de ajedrez para ejemplo
p1 = PiezaAjedrez("Blanco", Coordenada("A", 1))
p2 = PiezaAjedrez("Negro", Coordenada("E", 5))

print(p1)
print(p2)
