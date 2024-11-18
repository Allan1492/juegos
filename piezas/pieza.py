from .coordenada import Coordenada

# Superclase 
class Pieza:
    def __init__(self, color, coordenada):
        self.color = color
        self.coordenada = coordenada  

    def __repr__(self):
        return f"{self.color} Pieza en {self.coordenada}"

    