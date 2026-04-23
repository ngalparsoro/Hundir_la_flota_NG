
import numpy as np

from variables import TAMANO, BARCOS
from classBarco import Barco
from classTablero import Tablero

# FUNCIONES DEL JUEGO

def crear_barcos():
    """Crea la lista de barcos según configuración"""
    lista = []
    for nombre, eslora, cantidad in BARCOS:
        for i in range(cantidad):
            lista.append(Barco(nombre, eslora))
    return lista

def turno_jugador(tablero_maquina, vista_maquina):
    """Turno del jugador"""
    print("\n" + "_"*100)
    print("\nTU TURNO")
    print("_"*100)
    
    vista_maquina.mostrar(ocultar = False)
    
    while True:
        try:
            entrada = input("\nDisparar (fila columna): ")
            fila, col = map(int, entrada.split())
            if 0 <= fila < TAMANO and 0 <= col < TAMANO:
                break
            print(f"Usa números 0-{TAMANO-1}")
        except:
            print("Error, mete dos números separados: 5 3")
    
    resultado = tablero_maquina.disparar(fila, col)
    vista_maquina.rejilla[fila, col] = tablero_maquina.rejilla[fila, col]
    
    if resultado == "repetido":
        print("Ya disparaste ahí. Pierdes turno.")
        input("\nPresiona Enter.")
        return False
    elif resultado == "agua":
        print("¡AGUA!")
        input("\nPresiona Enter.")
        return False
    elif resultado[0] == "tocado":
        print(f"¡TOCADO! ({resultado[1]})")
        print("¡Repites!")
        input("\nPresiona Enter.")
        return True
    elif resultado[0] == "hundido":
        print(f"¡HUNDIDO! ({resultado[1]})")
        print("¡Repites!")
        input("\nPresiona Enter.")
        return True

def turno_maquina(tablero_jugador, vista_maquina):
    """Turno de la máquina"""
    print("\n" + "_"*100)
    print("TURNO DE LA MÁQUINA")
    print("_"*100)
    print("\n TABLERO DE LA MAQUINA")
    tablero_jugador.mostrar(ocultar = False)
    
    # Disparo aleatorio
    while True:
        fila = np.random.randint(0, TAMANO)
        col = np.random.randint(0, TAMANO)
        if vista_maquina.rejilla[fila, col] not in ["X", "O"]:
            break
    
    resultado = tablero_jugador.disparar(fila, col)
    vista_maquina.rejilla[fila, col] = tablero_jugador.rejilla[fila, col]
    
    print(f"\nMáquina disparó a ({fila}, {col})")

    input("\nLa maquina ya ha disparado, presiona Enter para pasar a tu turno")
    
    if resultado == "agua":
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