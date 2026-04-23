import numpy as np

from variables import TAMANO, BARCOS
from classBarco import Barco
from classTablero import Tablero
from functions import crear_barcos, turno_jugador, turno_maquina



# PROGRAMA PRINCIPAL

def jugar():
    print("\n" + "_"*100)
    print("¡HUNDIR LA FLOTA!")
    print("_"*100)
    print("\nBarcos:")
    for nombre, eslora, cantidad in BARCOS:
        print(f"  • {cantidad} x {nombre} (tamaño {eslora})")
    
    # Crear tableros
    jugador = Tablero()
    maquina = Tablero()
    vista_maquina = Tablero()
    vista_jugador = Tablero()
    
    # Colocar barcos del jugador
    print("\n" + "_"*100)
    print("COLOCA TUS BARCOS")
    print("_"*100)
    
    for barco in crear_barcos():
        while True:
            print(f"\nColocando {barco.nombre} (tamaño {barco.eslora})")
            jugador.mostrar(ocultar=False)
            
            try:
                entrada = input("\nPosición (fila columna): ")
                fila, col = map(int, entrada.split())
                h = input("Horizontal? (s/n): ").lower() == 's'
                
                if jugador.colocar_barco(barco, fila, col, h):
                    print("¡Colocado!")
                    break
                else:
                    print("No se puede. Intenta otra posición.")
            except:
                print("Ejemplo: 5 3")
    
    # Colocar barcos de la máquina
    print("\nLa máquina coloca sus barcos...")
    for barco in crear_barcos():
        maquina.colocar_aleatorio(barco)
    
    input("\n¡COMIENZA LA BATALLA! Presiona Enter...")
    
    # Juego
    turno_jugador_activo = True
    
    while True:
        print("\nTU TABLERO:")
        maquina.mostrar(ocultar=False) # Se visualizan los barcos en la demo.
        #vista_jugador.mostrar()
        print("\n TABLERO DE LA MAQUINA")
        jugador.mostrar(ocultar=False)
        
        if turno_jugador_activo:
            print("\n" *2)
            repite = turno_jugador(maquina, vista_maquina)
            
            if maquina.todos_hundidos():
                print("\n" + "_"*100)
                print("ZORIONAK WINNER")
                print("_"*100)
                break
            
            if not repite:
                turno_jugador_activo = False
        else:
            input("\nLa maquina ya ha disparado, presiona Enter para pasar a tu turno")
            repite = turno_maquina(jugador, vista_jugador)
            
            if jugador.todos_hundidos():
                print("\n" + "100"*40)
                print("GAME OVER.")
                print("_"*100)
                break
            
            if not repite:
                turno_jugador_activo = True


# Ejecutar juego
if __name__ == "__main__":
    jugar()