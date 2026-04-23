'''from classBarco import Barco'''


# CLASE BARCO
class Barco:
    def __init__(self, nombre, eslora):
        self.nombre = nombre
        self.eslora = eslora
        self.posiciones = []
        self.golpes = 0
    
    def hundido(self):
        return self.golpes >= self.eslora
