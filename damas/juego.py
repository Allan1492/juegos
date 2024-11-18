from juegos.piezas.pieza import Pieza
from juegos.piezas.coordenada import Coordenada

# Subclase de Pieza para el juego de Damas
class PiezaDamas(Pieza):
    def __init__(self, color, coordenada):
        # En Damas, las piezas se mueven sobre casillas negras numeradas del 1 al 12
        super().__init__(color, coordenada)

# Crear algunas piezas de Damas para ejemplo
p1 = PiezaDamas("Blanco", Coordenada(1, 1))
p2 = PiezaDamas("Negro", Coordenada(6, 4))

print(p1)
print(p2)
