'''from classTablero import Tablero'''

import numpy as np

from variables import TAMANO, BARCOS

# CLASE TABLERO

class Tablero:
    def __init__(self):
        self.agua = " "
        self.barco = "B"
        self.tocado = "X"
        self.fallado = "#"
        
        self.rejilla = np.full((TAMANO, TAMANO), self.agua, dtype=str)
        self.barcos = []
    
    def colocar_barco(self, barco, fila, col, horizontal):
        """Coloca un barco si es posible"""
        posiciones = []
        
        if horizontal:
            if col + barco.eslora > TAMANO:
                return False
            for i in range(barco.eslora):
                if self.rejilla[fila, col + i] != self.agua:
                    return False
                posiciones.append((fila, col + i))
        else:
            if fila + barco.eslora > TAMANO:
                return False
            for i in range(barco.eslora):
                if self.rejilla[fila + i, col] != self.agua:
                    return False
                posiciones.append((fila + i, col))
        
        # Colocar
        for f, c in posiciones:
            self.rejilla[f, c] = self.barco
        barco.posiciones = posiciones
        self.barcos.append(barco)
        return True
    
    def colocar_aleatorio(self, barco):
        """Coloca un barco en posición aleatoria"""
        while True:
            fila = np.random.randint(0, TAMANO)
            col = np.random.randint(0, TAMANO)
            horizontal = np.random.choice([True, False])
            if self.colocar_barco(barco, fila, col, horizontal):
                break
    
    def disparar(self, fila, col):
        """Procesa un disparo"""
        celda = self.rejilla[fila, col]
        
        if celda == self.tocado or celda == self.fallado:
            return "repetido"
        
        if celda == self.agua:
            self.rejilla[fila, col] = self.fallado
            return "agua"
        
        if celda == self.barco:
            self.rejilla[fila, col] = self.tocado
            for barco in self.barcos:
                if (fila, col) in barco.posiciones:
                    barco.golpes += 1
                    if barco.hundido():
                        return "hundido", barco.nombre
                    return "tocado", barco.nombre
    
    def todos_hundidos(self):
        return all(b.hundido() for b in self.barcos)
    
    def mostrar(self, ocultar=True):
        """Muestra el tablero"""
        print("\n    ", end="")
        for j in range(TAMANO):
            print(f"{j}", end="  ")
        print("\n   +" + "---" * TAMANO)
        
        for i in range(TAMANO):
            print(f"{i:2d} | ", end="")
            for j in range(TAMANO):
                celda = self.rejilla[i, j]
                if ocultar and celda == self.barco:
                    print(f" {self.agua}", end=" ")
                else:
                    print(f" {celda}", end=" ")
            print()
    