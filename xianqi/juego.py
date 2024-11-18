from juegos.piezas.pieza import Pieza
from juegos.piezas.coordenada import Coordenada

# Subclase de Pieza para el juego de Xianqi (Ajedrez Chino)
class PiezaXianqi(Pieza):
    def __init__(self, color, coordenada):
        # las piezas están en los vértices, 
        super().__init__(color, coordenada)

# Crear algunas piezas de Xianqi para ejemplo
p1 = PiezaXianqi("Rojo", Coordenada(1, 1))
p2 = PiezaXianqi("Negro", Coordenada(2, 3))

print(p1)
print(p2)
