'''from functions import crear_barcos, turno_jugador, turno_maquina'''

import numpy as np

from variables import TAMANO, BARCOS
from classBarco import Barco
from classTablero import Tablero

# FUNCIONES DEL JUEGO

def crear_barcos():
    """Crea la lista de barcos según configuración"""
    lista = []
    for nombre, eslora, cantidad in BARCOS:
        for _ in range(cantidad):
            lista.append(Barco(nombre, eslora))
    return lista

def turno_jugador(tablero_enemigo, tablero_vista):
    """Turno del jugador"""
    print("\n" + "_"*100)
    print("TU TURNO")
    print("_"*100)
    
    tablero_vista.mostrar(ocultar = False)
    
    while True:
        try:
            entrada = input("\nDisparar (fila columna): ")
            fila, col = map(int, entrada.split())
            if 0 <= fila < TAMANO and 0 <= col < TAMANO:
                break
            print(f"Usa números 0-{TAMANO-1}")
        except:
            print("Error, mete dos números separados: 5 3")
    
    resultado = tablero_enemigo.disparar(fila, col)
    tablero_vista.rejilla[fila, col] = tablero_enemigo.rejilla[fila, col]
    
    if resultado[0] == "repetido":
        print("Ya disparaste ahí. Pierdes turno.")
        return False
    elif resultado[0] == "agua":
        print("¡AGUA!")
        return False
    elif resultado[0] == "tocado":
        print(f"¡TOCADO! ({resultado[1]})")
        print("¡Repites!")
        return True
    elif resultado[0] == "hundido":
        print(f"¡HUNDIDO! ({resultado[1]})")
        print("¡Repites!")
        input("\nPresiona Enter...")
        return True

def turno_maquina(tablero_jugador, tablero_vista):
    """Turno de la máquina"""
    print("\n" + "_"*100)
    print("TURNO DE LA MÁQUINA")
    print("_"*100)
    
    # Disparo aleatorio
    while True:
        fila = np.random.randint(0, TAMANO)
        col = np.random.randint(0, TAMANO)
        if tablero_vista.rejilla[fila, col] not in ["X", "O"]:
            break
    
    resultado = tablero_jugador.disparar(fila, col)
    tablero_vista.rejilla[fila, col] = tablero_jugador.rejilla[fila, col]
    
    print(f"\nMáquina disparó a ({fila}, {col})")
    
    if resultado[0] == "agua":
        print("Falló. ¡Tu turno!")
        return False
    elif resultado[0] == "tocado":
        print(f"¡Te tocó! ({resultado[1]})")
        print("Repite turno...")
        return True
    elif resultado[0] == "hundido":
        print(f"¡Hundió tu {resultado[1]}!")
        print("Repite turno...")
        return True
    
    return False