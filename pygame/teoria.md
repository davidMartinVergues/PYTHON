 

# pygame

source [video youtube](https://www.youtube.com/watch?v=FfWpgLFMI7w&t=4370s)  

Instalamos el móduo `pygame`para crear juegos con python

```
pip install pygame
```
## Estructura del archivo

Tendremos dos partes bien diferenciadas:

1. Donde hacemos los imports y cargamos las imagenes q necesitaremos durante el juego
   ```python
    # Imports
    import pygame
    import os
    import time
    import random
    #--------FIN IMPORTS

    # habilitamos fuentes 
    pygame.font.init()
    #-------------------
    # create The screen
    WIDTH,HEIGHT = 750,750
    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
    ## title and icon on windows game
    pygame.display.set_caption('Space Invaders')
    icon = pygame.image.load(os.path.join('utils','ufo.png'))
    pygame.display.set_icon(icon)
    #-----------------------------------

    # Load images
    ## LOAD ENEMY IMAGES
    RED_SPACE_SHIP = pygame.image.load(os.path.join("utils","enemy_1.png"))
    GREEN_SPACE_SHIP = pygame.image.load(os.path.join("utils","enemy_2.png"))
    BLUE_SPACE_SHIP = pygame.image.load(os.path.join("utils","enemy_3.png"))
    ## LOAD PLAYER SHIP
    PLAYER_SHIP = pygame.image.load(os.path.join("utils","player.png"))
    ## lASER ENEMY
    RED_LASER = pygame.image.load(os.path.join('utils','pixel_laser_red.png'))
    GREEN_LASER = pygame.image.load(os.path.join('utils','pixel_laser_green.png'))
    BLUE_LASER = pygame.image.load(os.path.join('utils','pixel_laser_blue.png'))
    ## PLAYER laser
    PLAYER_LASER = pygame.image.load(os.path.join('utils','bullet.png'))
    ## BACKGROUND IMAGES
    BG = pygame.transform.scale(pygame.image.load(os.path.join('utils','background.png')), (WIDTH,HEIGHT))
    #-----------------END LOAD IMAGES
   ``` 

2. Definimos una función `main()` que contendrá la lógica del juego y que llamaremos al final del script.
   ```python
    def main():
        run = True
        FPS = 60

        level = 1
        lives= 5
        main_font = pygame.font.SysFont('comcsans',50)
        
        clock = pygame.time.Clock()
        
        def redraw_window():
            SCREEN.blit(BG,(0,0))
            pygame.display.update()
        
        while run:
            clock.tick(FPS) # para q se actualiza a la vez q el refresco de panatalla
            redraw_window()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


    main()
   ```  

## Ventana de juego

## Fijar tamaño, titulo, icono

```python
import pygame
import os

# create The screen
WIDTH,HEIGHT = 750,750
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
## title and icon on windows game
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load(os.path.join('utils','ufo.png'))
pygame.display.set_icon(icon)
#-----------------------------------
```
## Establecemos el fondo de la ventana de juego

Creamos una función que llamaremos repetidamente para mostar la imagen de fondo.

- blit()
  llamamos al método `blit()`de la pantalla para dibujar la imagen de fondo (BG) a cogiendo como coordenadas (X=0,y=0) como la imagen puede q no coincida en tamaño la transformamos
- display.update()
  Hace q la imagen se muestre en la ventana  

```python
BG = pygame.transform.scale(pygame.image.load(os.path.join('utils','background.png')), (WIDTH,HEIGHT))

def redraw_window():
    SCREEN.blit(BG,(0,0))
    pygame.display.update()
```

## mostramos Info

Para ello necesitamos habilitar fuentes , lo hacemos justo después de los imports.

```python
pygame.font.init()
```
Generamos un reloj, para contabilizar el tiempo

```python
clock = pygame.time.Clock()
```

