import numpy as np

from variables import TAMANO, BARCOS
from classBarco import Barco
from classTablero import Tablero
from functions import crear_barcos, turno_jugador, turno_maquina



# PROGRAMA PRINCIPAL

def jugar():
    print("\n" + "="*40)
    print("¡HUNDIR LA FLOTA!")
    print("="*40)
    print("\nBarcos:")
    for nombre, eslora, cantidad in BARCOS:
        print(f"  • {cantidad} x {nombre} (tamaño {eslora})")
    
    # Crear tableros
    jugador = Tablero()
    maquina = Tablero()
    vista_maquina = Tablero()
    vista_jugador = Tablero()
    
    # Colocar barcos del jugador
    print("\n" + "="*40)
    print("COLOCA TUS BARCOS")
    print("="*40)
    
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
        # Mostrar estado
        stats = jugador.obtener_estadisticas()
        print(f"\nTus barcos restantes: {stats['vivos']}/{stats['total']}")
        
        print("\nTU TABLERO:")
        maquina.mostrar(ocultar=False) # Se visualizan los barcos en la demo.
        #vista_jugador.mostrar()
        print("\n TABLERO DE LA MAQUINA")
        jugador.mostrar(ocultar=False)
        
        if turno_jugador_activo:
            print("\n ¡ES TU TURNO!")
            repite = turno_jugador(maquina, vista_maquina)
            
            if maquina.todos_hundidos():
                print("\n" + "="*40)
                print("¡FELICIDADES! ¡HAS GANADO!")
                print("="*40)
                break
            
            if not repite:
                turno_jugador_activo = False
        else:
            repite = turno_maquina(jugador, vista_jugador)
            
            if jugador.todos_hundidos():
                print("\n" + "="*40)
                print("GAME OVER. Perdiste.")
                print("="*40)
                break
            
            if not repite:
                turno_jugador_activo = True


# Ejecutar juego
if __name__ == "__main__":
    jugar()