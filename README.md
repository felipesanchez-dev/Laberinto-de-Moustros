# 🐉 Laberinto de Moustros

¡Bienvenido a **Laberinto de Moustros**!  
Este es un juego **open source** desarrollado como parte de una prueba técnica para el puesto de tutor de Python.  
El proyecto utiliza **Programación Orientada a Objetos (POO)** y la famosa librería **PyGame** para crear una experiencia divertida y didáctica.

---
## 📁 Estructura del Proyecto
```bash
Laberinto de Moustros/
│
├── .gitignore         
├── README.md            # 📖 Documentación y guía del proyecto
├── requirements.txt     # 📦 Dependencias necesarias para ejecutar el juego
├── .vscode/
│   └── settings.json    # ⚙️ Configuración para Visual Studio Code
│
├── client/         
│   ├── graphics/        # 🎨 Gráficos y sprites
│   │   ├── font/        # 🔤 Fuentes tipográficas
│   │   ├── grass/       # 🌱 Sprites de césped
│   │   ├── monsters/    # 👾 Sprites de monstruos
│   │   ├── objects/     # 🗝️ Objetos del mapa
│   │   ├── particles/   # ✨ Efectos de partículas
│   │   ├── player/      # 🧑‍🎮 Sprites del jugador
│   │   ├── test/        # 🧪 Recursos de prueba
│   │   ├── tilemap/     # 🧩 Tiles del mapa
│   │   └── weapons/     # ⚔️ Sprites de armas
│   │
│   ├── map/             # 🗺️ Mapas en formato CSV
│   │   ├── map_Details.csv
│   │   ├── map_Entities.csv
│   │   ├── map_Floor.csv
│   │   ├── map_FloorBlocks.csv
│   │   ├── map_Grass.csv
│   │   └── map_Objects.csv
│   │
│   └── src/             # 💻 Código fuente principal
│       ├── debug.py         # 🐞 Depuración en pantalla
│       ├── enemy.py         # 👹 Lógica de enemigos
│       ├── entity.py        # 🧬 Entidad base (jugador, enemigos)
│       ├── level.py         # 🏞️ Lógica del nivel y mapa
│       ├── magic.py         # 🪄 Magias y habilidades
│       ├── main.py          # 🚀 Punto de entrada del juego
│       ├── particles.py     # 💨 Efectos de partículas animadas
│       ├── player.py        # 🧑‍🎮 Lógica del jugador
│       ├── settings.py      # ⚙️ Configuración general y constantes
│       ├── support.py       # 🛠️ Funciones de soporte (carga de recursos)
│       ├── tile.py          # 🧱 Lógica de los tiles del mapa
│       ├── ui.py            # 🖥️ Interfaz gráfica de usuario
│       ├── upgrade.py       # ⬆️ Menú de mejoras del jugador
│       ├── weapon.py        # ⚔️ Lógica de armas
│       └── __pycache__/     # 🗑️ Archivos temporales de Python
```
<br> <br>

# 📄 Documentación
##  📁 `main.py`
> **Ubicación:** `client/src/main.py`  
> **Propósito:** Punto de entrada principal del juego **Laberinto de Moustros**. Inicializa la ventana, el bucle principal y la música, y gestiona los eventos globales.

---

## Tabla de Contenidos
- [1. Importaciones](#1-importaciones)
- [2. Clase Game](#2-clase-game)
  - [2.1. `__init__`](#21-__init__)
  - [2.2. `run`](#22-run)
- [3. Ejecución del Juego](#3-ejecución-del-juego)
- [4. Eventos y Controles](#4-eventos-y-controles)
- [5. Notas sobre el Audio](#5-notas-sobre-el-audio)
- [6. Dependencias](#6-dependencias)
- [7. Ejemplo de Ejecución](#7-ejemplo-de-ejecución)
---
## 1. Importaciones
```python
import socket
import pygame, sys
from settings import *
from level import Level
```
- **socket:** (No utilizado directamente en este archivo, pero preparado para futuras funciones de red).
- **pygame, sys:** Librerías principales para gráficos, eventos y cierre del juego.
- **settings:** Importa constantes globales como `WIDTH`, `HEIGTH`, `FPS`, `WATER_COLOR`, etc.
- **Level:** Clase que gestiona la lógica del nivel, sprites y el jugador.
---
## 2. Clase `Game`
La clase principal que representa el ciclo de vida del juego.
### 2.1. `__init__`
```python
def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
    pygame.display.set_caption('Laberinto de Moustros')
    self.clock = pygame.time.Clock()
    self.level = Level()
    main_sound = pygame.mixer.Sound('../audio/main.ogg')
    main_sound.set_volume(0.2)
    main_sound.play(loops = -1)
```
- **Inicialización de Pygame:** Prepara todos los módulos de Pygame.
- **Ventana:** Crea la ventana del juego con el tamaño definido en `settings.py`.
- **Título:** Establece el nombre de la ventana.
- **Reloj:** Controla los FPS del juego.
- **Nivel:** Instancia la clase `Level`, que contiene toda la lógica del mapa, jugador y enemigos.
- **Música:** Carga y reproduce en bucle la música principal del juego.
---
### 2.2. `run`
```python
def run(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    self.level.toggle_menu()

        self.screen.fill(WATER_COLOR)
        self.level.run()
        pygame.display.update()
        self.clock.tick(FPS)
```
- **Bucle principal:** Se ejecuta indefinidamente hasta que el usuario cierra la ventana.
- **Gestión de eventos:**
  - **Salir:** Si el usuario cierra la ventana, termina el programa limpiamente.
  - **Tecla `M`:** Alterna el menú de mejoras del jugador.
- **Dibujo:**
  - **Fondo:** Rellena la pantalla con el color del agua (`WATER_COLOR`).
  - **Nivel:** Llama al método `run()` de la clase `Level` para actualizar y dibujar todos los elementos del juego.
  - **Actualización:** Refresca la pantalla y mantiene la velocidad de fotogramas constante.
---
## 3. Ejecución del Juego
```python
if __name__ == '__main__':
    game = Game()
    game.run()
```
- Si el archivo se ejecuta directamente, crea una instancia de `Game` y llama a su método `run()` para iniciar el juego.
---
## 4. Eventos y Controles
- **Cerrar ventana:** Sale del juego.
- **Tecla `M`:** Abre/cierra el menú de mejoras del jugador.
---
## 5. Notas sobre el Audio
- El archivo de audio principal debe estar en `client/audio/main.ogg`.
- El volumen está reducido al 20% para no ser invasivo.
- La música se reproduce en bucle infinito durante toda la partida.
---
## 6. Dependencias
- [pygame](https://www.pygame.org/)  
- Python 3.x  
- Archivos y carpetas definidos en `settings.py` y `level.py`
---
## 7. Ejemplo de Ejecución
```bash
python client/src/main.py
```
---
## 📝 Resumen

Este archivo es el **corazón** del juego: inicializa la ventana, la música, el bucle principal y delega la lógica del juego a la clase `Level`. Es el punto de partida para cualquier modificación global del comportamiento del juego.

---

##  📁 `player.py`

> **Ubicación:** `client/src/player.py`  
> **Propósito:** Define la clase `Player`, que representa al jugador principal del juego, gestionando su movimiento, ataques, magias, animaciones, estadísticas y lógica de muerte/reinicio.

---

## 🧩 Paradigma: Programación Orientada a Objetos (POO)

Este archivo es un claro ejemplo de **POO** en Python.  
La clase `Player` hereda de la clase base `Entity`, encapsulando atributos y comportamientos propios del jugador.  
Esto permite reutilizar y extender funcionalidades, facilitando la mantenibilidad y escalabilidad del código.

---

## Tabla de Contenidos

- [1. Importaciones](#1-importaciones)
- [2. Clase Player](#2-clase-player)
  - [2.1. Inicialización y atributos](#21-inicialización-y-atributos)
  - [2.2. Métodos principales](#22-métodos-principales)
- [3. Principales responsabilidades](#3-principales-responsabilidades)
- [4. Notas sobre el diseño](#4-notas-sobre-el-diseño)
- [5. Ejemplo de uso](#5-ejemplo-de-uso)

---

## 1. Importaciones

```python
import pygame
from settings import *           # Constantes y diccionarios globales
from support import import_folder
from entity import Entity        # Clase base para entidades móviles
```

---

## 2. Clase `Player`

### 2.1. Inicialización y atributos

- **Herencia:**  
  `Player` hereda de `Entity`, lo que le otorga capacidades de movimiento, animación y colisiones.
- **Atributos principales:**
  - `image`, `rect`, `hitbox`: Gráficos y colisiones.
  - `animations`: Diccionario de animaciones por estado.
  - `status`: Estado actual (ej: 'down', 'up_attack', etc).
  - `attacking`, `attack_cooldown`, `attack_time`: Control de ataques.
  - `weapon`, `magic`: Arma y magia equipadas, con índices para cambiar entre ellas.
  - `stats`, `max_stats`, `upgrade_cost`: Estadísticas y mejoras del jugador.
  - `health`, `energy`, `exp`, `speed`: Valores actuales de vida, energía, experiencia y velocidad.
  - `vulnerable`, `hurt_time`, `invulnerability_duration`: Control de daño e invulnerabilidad temporal.
  - `is_dead`, `trigger_game_restart`: Lógica de muerte y reinicio del juego.

### 2.2. Métodos principales

- **import_player_assets:**  
  Carga todas las animaciones del jugador desde los recursos gráficos.

- **input:**  
  Gestiona la entrada del usuario (movimiento, ataque, magia, cambio de arma/magia).  
  Si el jugador está muerto, ignora las entradas.

- **get_status:**  
  Actualiza el estado (`status`) del jugador según su movimiento y acciones.

- **cooldowns:**  
  Controla los tiempos de espera para ataques, cambios de arma/magia e invulnerabilidad.

- **animate:**  
  Actualiza el frame de animación según el estado actual y aplica efectos visuales (parpadeo al recibir daño).

- **get_full_weapon_damage / get_full_magic_damage:**  
  Calculan el daño total considerando estadísticas y arma/magia equipada.

- **energy_recovery:**  
  Recupera energía automáticamente según la estadística de magia.

- **update:**  
  Método principal llamado cada frame.  
  Gestiona entradas, actualizaciones de estado, movimiento, recuperación de energía, lógica de muerte y animación.

---

## 3. Principales responsabilidades

- **Movimiento y animación:**  
  El jugador puede moverse en 4 direcciones y tiene animaciones para cada estado (idle, ataque, etc).

- **Ataques y magias:**  
  Permite atacar con armas o lanzar magias, cada una con su propio cooldown y efectos.

- **Gestión de estadísticas:**  
  Vida, energía, ataque, magia, velocidad y experiencia, con posibilidad de mejorar mediante el menú de upgrades.

- **Invulnerabilidad temporal:**  
  Tras recibir daño, el jugador es invulnerable durante un breve periodo (efecto parpadeo).

- **Cambio de arma y magia:**  
  El jugador puede alternar entre diferentes armas y magias disponibles.

- **Muerte y reinicio:**  
  Si la vida llega a 0, se activa la bandera `is_dead` y se llama a la función de reinicio del juego.

---

## 4. Notas sobre el diseño

- **Extensible:**  
  Gracias a la herencia y la separación de responsabilidades, es fácil añadir nuevas armas, magias o comportamientos.

- **Encapsulamiento:**  
  Los atributos y métodos están bien organizados, facilitando el mantenimiento y la comprensión del código.

- **Reutilización:**  
  Al heredar de `Entity`, se evita duplicar lógica común entre jugador y enemigos.

---

## 5. Ejemplo de uso

```python
# Creación de un jugador en el juego (dentro de Level o similar)
player = Player(
    pos=(100, 100),
    groups=all_sprites,
    obstacle_sprites=obstacles,
    create_attack=crear_ataque,
    destroy_attack=destruir_ataque,
    create_magic=crear_magia,
    trigger_game_restart=reiniciar_juego
)
```

---

## 📝 Resumen

El archivo `player.py` es un pilar fundamental del juego, implementando toda la lógica y comportamiento del personaje principal bajo un enfoque orientado a objetos.  
Permite una experiencia de juego fluida, personalizable y fácilmente ampliable.

---

##  📁 `ui.py`
> **Ubicación:** `client/src/ui.py`  
> **Propósito:** Gestiona y dibuja la interfaz gráfica de usuario (UI) del juego, mostrando barras de vida, energía, experiencia, armas y magias equipadas.

---

## 🧩 Paradigma: Programación Orientada a Objetos (POO)

La clase `UI` encapsula toda la lógica y los datos relacionados con la interfaz gráfica del jugador.  
Esto permite separar claramente la presentación visual del resto de la lógica del juego, facilitando la mantenibilidad y la extensión del código.

---

## Tabla de Contenidos

- [1. Importaciones](#1-importaciones)
- [2. Clase UI](#2-clase-ui)
  - [2.1. Inicialización y atributos](#21-inicialización-y-atributos)
  - [2.2. Métodos principales](#22-métodos-principales)
- [3. Principales responsabilidades](#3-principales-responsabilidades)
- [4. Notas sobre el diseño](#4-notas-sobre-el-diseño)
- [5. Ejemplo de uso](#5-ejemplo-de-uso)

---

## 1. Importaciones

```python
import pygame
from settings import *  # Constantes y diccionarios globales
```

---

## 2. Clase `UI`

### 2.1. Inicialización y atributos

- **display_surface:**  
  Superficie principal donde se dibuja la UI (la ventana del juego).
- **font:**  
  Fuente utilizada para los textos de la interfaz.
- **health_bar_rect, energy_bar_rect, experience_bar_rect:**  
  Rectángulos que definen la posición y tamaño de las barras de vida, energía y experiencia.
- **weapon_graphics, magic_graphics:**  
  Listas de imágenes de armas y magias, cargadas desde los recursos definidos en `settings.py`.

### 2.2. Métodos principales

- **show_bar(current, max_amount, bg_rect, color):**  
  Dibuja una barra de progreso (vida, energía, experiencia) con su fondo y borde.

- **show_exp(exp):**  
  Muestra la cantidad actual de experiencia en la esquina inferior derecha de la pantalla.

- **selection_box(left, top, has_switched):**  
  Dibuja una caja de selección para indicar el arma o magia equipada, resaltando si ha habido un cambio reciente.

- **weapon_overlay(weapon_index, has_switched):**  
  Muestra el sprite del arma equipada en la interfaz, usando la caja de selección.

- **magic_overlay(magic_index, has_switched):**  
  Muestra el sprite de la magia equipada en la interfaz, usando la caja de selección.

- **display(player):**  
  Método principal que dibuja todos los elementos de la interfaz según el estado actual del jugador.

---

## 3. Principales responsabilidades

- **Visualización de estadísticas:**  
  Muestra de forma clara y visual la vida, energía y experiencia del jugador.
- **Equipamiento:**  
  Indica qué arma y magia están equipadas actualmente, con sprites y cajas de selección.
- **Feedback visual:**  
  Resalta los cambios de arma/magia y muestra la experiencia de forma destacada.

---

## 4. Notas sobre el diseño

- **Separación de responsabilidades:**  
  Toda la lógica de la interfaz está contenida en una sola clase, facilitando su modificación y extensión.
- **Escalabilidad:**  
  Es sencillo añadir nuevas barras, iconos o elementos visuales siguiendo el mismo patrón.
- **Reutilización:**  
  Los métodos como `show_bar` y `selection_box` pueden ser reutilizados para otros elementos visuales.

---

## 5. Ejemplo de uso

```python
# En el bucle principal del juego, tras actualizar el estado del jugador:
ui = UI()
...
ui.display(player)
```

---

## 📝 Resumen

El archivo `ui.py` es esencial para la experiencia de usuario, proporcionando información visual clara y atractiva sobre el estado del jugador y sus recursos.  
Su diseño orientado a objetos permite mantener el código organizado y fácilmente ampliable.

---

# Guía de Instalación: Laberinto de Monstruos

Esta guía te ayudará a configurar el entorno de desarrollo para el proyecto "Laberinto de Monstruos". Se recomienda el uso de entornos virtuales de Python para gestionar las dependencias del proyecto de forma aislada.

## Requisitos Previos

* **Python 3.x:** Asegúrate de tener Python 3 instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/).
* **Git:** Necesitarás Git para clonar el repositorio. Puedes descargarlo desde [git-scm.com](https://git-scm.com/).

## Pasos de Instalación

### 1. Clonar el Repositorio

Primero, clona el repositorio del proyecto en tu máquina local. Abre tu terminal o consola y ejecuta el siguiente comando:

```sh
git clone https://github.com/felipesanchez-dev/Laberinto-de-Moustros.git
```

Una vez completada la clonación, navega al directorio del proyecto:

```sh
cd Laberinto-de-Moustros
```
*Es importante que los siguientes comandos se ejecuten desde la raíz de este directorio (`Laberinto-de-Moustros`).*

### 2. Configurar el Entorno Virtual

Crear un entorno virtual es una buena práctica para aislar las dependencias de tu proyecto.

#### macOS

1.  **Crea el entorno virtual:**
    ```bash
    python3 -m venv venv
    ```
2.  **Activa el entorno virtual:**
    ```bash
    source venv/bin/activate
    ```
    *Tu prompt de terminal debería cambiar para indicar que el entorno `(venv)` está activo.*

#### Windows

1.  **Crea el entorno virtual:**
    ```bash
    python -m venv venv
    ```
    *(Si tienes múltiples versiones de Python, podrías necesitar usar `py -3 -m venv venv` o `python3 -m venv venv` si `python` no apunta a Python 3).*
2.  **Activa el entorno virtual:**
    * Si usas **Command Prompt (CMD)**:
        ```bash
        venv\Scripts\activate.bat
        ```
    * Si usas **PowerShell**:
        ```bash
        .\venv\Scripts\Activate.ps1
        ```
        *(Nota: Si encuentras un error relacionado con la política de ejecución de scripts en PowerShell, puede que necesites ejecutar `Set-ExecutionPolicy Unrestricted -Scope Process` y luego intentar activar el entorno nuevamente).*
    * Si usas **Git Bash** (u otro emulador de bash):
        ```bash
        source venv/Scripts/activate
        ```
    *Tu prompt de terminal debería cambiar para indicar que el entorno `(venv)` está activo.*

#### Linux

1.  **Crea el entorno virtual:**
    ```bash
    python3 -m venv venv
    ```
2.  **Activa el entorno virtual:**
    ```bash
    source venv/bin/activate
    ```
    *Tu prompt de terminal debería cambiar para indicar que el entorno `(venv)` está activo.*

### 3. Instalar Dependencias

Con el entorno virtual **activado** (deberías ver `(venv)` al inicio de tu prompt), instala las dependencias del proyecto listadas en el archivo `requirements.txt`:

```sh
pip install -r requirements.txt
```

### 4. Ejecutar la Aplicación

Una vez que las dependencias se hayan instalado correctamente y con el entorno virtual aún activado, puedes ejecutar la aplicación cliente. Navega al directorio del cliente y ejecuta el script principal:

```sh
cd client/src
python main.py
```

O, alternativamente, puedes ejecutarlo directamente desde la raíz del proyecto (`Laberinto-de-Moustros`):

```sh
python client/src/main.py
```

### 5. Desactivar el Entorno Virtual

Cuando hayas terminado de trabajar en el proyecto, puedes desactivar el entorno virtual ejecutando el siguiente comando en tu terminal:

```bash
deactivate
```
Esto te devolverá a tu shell global de Python.

<br> <br>
## ✨ Imagenes

| ![Pantalla del juego](https://github.com/felipesanchez-dev/Laberinto-de-Moustros/blob/main/image/game.jpg) | ![Captura 2](https://github.com/felipesanchez-dev/Pronostico-del-Clima/blob/main/assets/Capturas/app2.jpg) | ![Captura 3](https://github.com/felipesanchez-dev/Pronostico-del-Clima/blob/main/assets/Capturas/app3.jpg) |
|------------------------------------------|------------------------------------------|------------------------------------------|


# 📌 Nota Importante sobre Recursos Gráficos

Para acelerar el desarrollo de este proyecto, se han utilizado recursos visuales del excelente paquete **[Ninja Adventure Asset Pack](https://pixel-boy.itch.io/ninja-adventure-asset-pack)**, una creación de **Pixel-boy**.

> ✨ ¡Todo el reconocimiento y los créditos por el arte son para ellos! 🎨

---

## 💬 ¡Conectemos!

¿Tienes alguna pregunta, ideas innovadoras o simplemente te apetece compartir tu experiencia desarrollando proyectos similares? ¡Será un placer saber de ti! 😊 No dudes en contactarme a través de los siguientes canales:

* 📧 **Correo Electrónico:** [felipe@felipesanchezdev.site](mailto:felipe@felipesanchezdev.site)
* 🔗 **LinkedIn:** [felipereyessa](https://www.linkedin.com/in/felipereyessa)
* 🌐 **Sitio Web:** [felipesanchezdev.site](https://felipesanchezdev.site)
