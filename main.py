import numpy as np

from variables import TAMANO, BARCOS
from classBarco import Barco
from classTablero import Tablero
from functions import crear_barcos, turno_jugador, turno_maquina

# PROGRAMA PRINCIPAL

def jugar():
    print("\n" + "_"*100)
    print("\n¡HUNDIR LA FLOTA!")
    print("_"*100)
    print("\nBarcos:")
    for nombre, eslora, cantidad in BARCOS:
        print(f"  • {cantidad} x {nombre} (tamaño {eslora})")
    
    # Crear tableros
    tablero_jugador = Tablero()
    tablero_maquina = Tablero()
    vista_maquina = Tablero()
    vista_jugador = Tablero()
    
    # Colocar barcos del jugador
    print("\n" + "_"*100)
    print("\n COLOCA TUS BARCOS")
    print("_"*100)
    
    for barco in crear_barcos():
        while True:
            print(f"\nColocando {barco.nombre} (eslora {barco.eslora})")
            tablero_jugador.mostrar(ocultar=False)
            
            try:
                entrada = input("\nPosición (fila columna): ")
                fila, col = map(int, entrada.split())
                horizontal = input("Horizontal? (s/n): ").lower() 
                if horizontal == "s":
                    h = True
                elif horizontal == "n":
                    h = False
                else:
                    input("\nTienes que contestar s o n, intentalo de nuevo.")
                    continue
                
                if tablero_jugador.colocar_barco(barco, fila, col, h):
                    print("¡Colocado!")
                    break
                else:
                    print("\nNo se puede. Intenta otra posición.")
            except:
                print("Ejemplo: 5 3")
    
    # Colocar barcos de la máquina
    print("\nLa máquina coloca sus barcos...")
    for barco in crear_barcos():
        tablero_maquina.colocar_aleatorio(barco)
    
    input("\n¡COMIENZA LA BATALLA! Presiona Enter...")
    
    # Juego
    turno_jugador_activo = True
    
    while True:
        if turno_jugador_activo:
            print("\n" *2)
            repite = turno_jugador(tablero_maquina, vista_maquina)
            
            if tablero_maquina.todos_hundidos():
                print("_"*100)
                print("\n" + "_" * 42 + "ZORIONAK WINNER" + "_" * 42)
                print("\n" + "_" * 36 + "HAS HUNDIDO TODOS LOS BARCOS" + "_" * 36)
                print("_"*100)
                print("\n"*5)
                break
            
            if not repite:
                turno_jugador_activo = False
        else:
            repite = turno_maquina(tablero_jugador, vista_jugador)
            
            if tablero_jugador.todos_hundidos():
                print("\n" + "100"*40)
                print("\nGAME OVER.")
                print("_"*100)
                break
            
            if not repite:
                turno_jugador_activo = True


# Ejecutar juego
if __name__ == "__main__":
    jugar()