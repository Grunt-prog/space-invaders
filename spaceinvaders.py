import tkinter as tk
import pygame
import random
import math
from pygame import mixer
# Intialize pygame
pygame.init()

# Create a screen for the game
screen = pygame.display.set_mode((800 , 600))  # length, width

# Title & Icon
pygame.display.set_caption("Ritesh's Game")
score_value = 0
# Score
font = pygame.font.Font("freesansbold.ttf" , 32)
textx = 10
texty = 10


# music
mixer.music.load("sounds/background.wav")
mixer.music.play(-1)

def texti(x , y):
    score = font.render("SCORE: " + str(score_value) , True , (255,255,255))
    screen.blit(score , (x , y))

def tec():
    gameover = font.render("GAME OVER" + "YOUR SCORE: " + str(score_value), True , (255,255,255))
    screen.blit(gameover , (175 , 300))
# Background
#bacimg = pygame.image.load("space-galaxy-background.jpg")
# Player
playerimage = pygame.image.load("img/001-spaceship.png")
playerx = 365
playery = 500
playx_change = 0
def player(x,y):
    screen.blit(playerimage , (x,y))



# ENEMY
enemyimage = []
enemyx = []
enemyy =  []
enemyx_change = []
enemyy_change = []
no_of_enemies = 10
for i in range(no_of_enemies):
    enemyimage.append(pygame.image.load("img/001-skull.png"))
    enemyx.append(random.randint(0 , 780))
    enemyy.append(random.randint(50 ,150))
    enemyx_change.append(0.5)
    enemyy_change.append(100)
    
    
def enemy(x ,y ,i):
    screen.blit(enemyimage[i] , (x,y))


# Bullet
bulletimage = pygame.image.load("img/001-bullet.png")
bulletx = 0
bullety = 500
bulletx_change = 0
bullety_change = 1.5
bullet_state = "ready"

def fire_bullet(x , y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bulletimage , (x + 20 , y + 20))


#collision
def iscollision(enemyx , enemyy , bulletx , bullety):
    distance = math.sqrt(math.pow((enemyx - bulletx) , 2) + math.pow((enemyy - bullety) , 2))
    if distance < 25:
        return True
    else:
        return False

# game loop
running = True
while running:  
    # SETTING BACKGROUND COLOUR
    screen.fill((0 , 0 , 0))    # black colour
    bacimg = pygame.image.load("img/bacimg.jfif")
    screen.blit(bacimg , (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playx_change = -0.9
            elif event.key == pygame.K_RIGHT:
                playx_change = 0.9
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletsound = mixer.Sound('sounds/laser.wav')
                    bulletsound.play()
                    bulletx = playerx
                    fire_bullet(bulletx , bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playx_change = 0



    playerx += playx_change

    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    
    for i in range(no_of_enemies):

        if enemyy[i] > 300:
            for j in range(no_of_enemies):
                enemyy[j] = 2000

            break


        enemyx[i] += enemyx_change[i]        
        if enemyx[i] <= 0:
            enemyx_change[i] = 0.1
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -0.1
            enemyy[i] += enemyy_change[i]
        coll = iscollision(enemyx[i] , enemyy[i] , bulletx , bullety)
        if coll:
            bullety = 500
            bullet_state = "ready"
            enemyx[i] = random.randint(0 , 770)
            enemyy[i] = random.randint(50 ,150)
            score_value = score_value + 1
            exsound = mixer.Sound('sounds/explosion.wav')
            exsound.play()
        enemy(enemyx[i] , enemyy[i] , i)


    if bullety <=0:
        bullety = 500
        bullet_state = "ready"



    if bullet_state == "fired":
        fire_bullet(bulletx , bullety)
        bullety -= bullety_change




    texti(textx , texty)
    player(playerx , playery)
    pygame.display.update()