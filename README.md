# Hundir la Flota — Versión en Python (Terminal)

Juego clásico **Hundir la Flota (Battleship)** implementado en Python, jugable desde la terminal.  
El jugador coloca sus barcos manualmente y compite contra una máquina que coloca y dispara de forma automática.

---

## Características principales

- Tablero de **10×10** configurable.
- Barcos con tamaños y cantidades definidas en `variables.py`.
- Colocación **manual** de barcos por parte del jugador.
- Colocación **aleatoria** de barcos por parte de la máquina.
- Sistema de disparos con:
  - "# Agua"
  - X Tocado
  - X Hundido
  - Repetición de turno al acertar
- Visualización del tablero del jugador y de la máquina.
- Lógica completa de victoria y derrota.

---

## Estructura del proyecto
```
📦 hundir_la_flota
├── classBarco.py
├── classTablero.py
├── functions.py
├── variables.py
├── main.py
└── README.md````


### `classBarco.py`
Define la clase `Barco`, con:
- Nombre  
- Eslora  
- Posiciones ocupadas  
- Golpes recibidos  
- Método `hundido()` para comprobar si el barco está destruido  

### `classTablero.py`
Gestiona el tablero:
- Representación con NumPy  
- Colocación manual y aleatoria de barcos  
- Procesamiento de disparos  
- Detección de hundimientos  
- Visualización del tablero con opción de ocultar barcos  

### `functions.py`
Incluye las funciones principales del juego:
- `crear_barcos()`  
- `turno_jugador()`  
- `turno_maquina()`  

### `variables.py`
Contiene la configuración del juego:

### `main.py`
Archivo principal que ejecuta el juego:
- Muestra menú inicial
- Permite colocar barcos al jugador
- Coloca barcos de la máquina
- Controla el bucle de turnos
- Detecta victoria o derrota

---

## ▶️ Cómo jugar

1. Ejecuta el archivo principal:
   ```bash
   python main.py
   
2. Coloca tus barcos indicando:
   - Fila y columna inicial
   - Orientación (horizontal o vertical)

3. Una vez colocados todos los barcos, comienza la batalla:
   - Introduce coordenadas para disparar (ej: `A5` o `3 7`)
   - Si aciertas, repites turno
   - Gana quien hunda **todos** los barcos del rival

---

## 🎯 Objetivo del juego

Hundir todos los barcos de la máquina **antes** de que ella hunda los tuyos.

---

## 🧩 Dependencias

- **Python 3.8+**
- **NumPy**
