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
WIDTH,HEIGHT = 1000,800
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

class Ship():
    def __init__(self, x, y, health= 100):
        self.x = x
        self.y = y
        self.health = health
        self.lasers= []
        self.cool_down_counter = 0
        
    def draw (self, window):
        
        window.blit(PLAYER_SHIP, (self.x,  self.y ))
        # dibujamos un rectangulo en la posición de la nave con un width heigth
        pygame.draw.rect(window, (255,0,0), (self.x,self.y+PLAYER_SHIP.get_height()+10,PLAYER_SHIP.get_width(),5 ))
    def get_width(self):
        return self.ship_img.get_width()
    def get_height(self):
        return self.ship_img.get_height()    
    
class Player(Ship):
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.ship_img =PLAYER_SHIP 
        self.laser_img= PLAYER_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):
    
    COLOR_ENEMY = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
    }
    
    def __init__(self,x,y,health=100, color):
        super().__init__(x,y,health)
        self.ship_img,self.laser_img= COLOR_ENEMY[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        
    def move(self, vel):
        self.y+= vel
         
        
        

def main():
    
    run = True
    FPS = 60
    
    player_speed = 5
    level = 1
    lives= 5
    main_font = pygame.font.SysFont('comcsans',50)
    
    player = Player(300,650)
    
    clock = pygame.time.Clock()
    
    def redraw_window():
       # background img
        SCREEN.blit(BG,(0,0))
       # pintamos una nave
        player.draw(SCREEN)
        #draw text
        lives_label = main_font.render(f'live: {lives}',1, (255,255,255))
        level_label = main_font.render(f'level: {level}',1, (255,255,255))
        SCREEN.blit(lives_label, (10,10))
        SCREEN.blit(level_label, (WIDTH-level_label.get_width() -10, 10))
       
        pygame.display.update()
    
    #  bucle principal del juego
    while run:
        clock.tick(FPS)
        redraw_window()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # movimiento de la nave
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and player.x - player_speed >0:
            player.x-=player_speed
        if key[pygame.K_RIGHT] and player.x +player.get_width()+ player_speed < WIDTH:
            player.x+=player_speed
        if key[pygame.K_UP] and player.y - player_speed >0:
            player.y-=player_speed
        if key[pygame.K_DOWN] and player.y+player.get_height() + player_speed < HEIGHT:
            player.y+=player_speed
            


main()
            
        

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     #changing background color 
#     #rgb(red, green, blue)
#     screen.fill((0,0,0))

    


     


 
 