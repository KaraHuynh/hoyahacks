import sys
import pygame
import random
import time
from pygame.locals import *

#Initializes game
pygame.init()


#Creates screen with given dimensions (L x W)
screen = pygame.display.set_mode((800,600)) 
#DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)




#Caption and Icon
pygame.display.set_caption("pop")
icon = pygame.image.load('Padoru.png')
pygame.display.set_icon(icon)
bg = pygame.image.load("background1.png")


#Creates Player
playerImg = pygame.image.load('character.png')
posX = 0
posY = 200
newPosX = 0
newPosY = 0
width = 600
height = 800
time = pygame.time.Clock


#Creates Falling Objects positions and speed
objImg = pygame.image.load('obj.png')
objSpeed = 5
objPosX = random.randrange(0,600)
objPosY = -500
    

#Random Falling Objects
def objects():
    screen.blit(objImg, (objPosX, objPosY))


#Player Position
def player():
    screen.blit(playerImg, (posX, posY))

playerAlive = True
lives = 3

def checkCollision(sprite1, sprite5):
    col = pygame.sprite.collide_rect(sprite1, sprite5)
    if col == True:
        lives -= 1


def title():
    title = pygame.image.load("title.png")
    screen.blit(title, (0, -400))


#Game loop
running = True
while running:
    title()

        


    #Set BG Colour using RGB code
    screen.fill((0,0,0))
    screen.blit(bg, (0, -400))
    
    for i in range(3):
        objects()
        objPosY = objPosY + objSpeed
        if(objPosY > 500):
            objPosY = -500
            objPosX = random.randrange(0,600)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        

        
        #deals with player position using the wasd keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                newPosX = -5
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                newPosX = 5
            if event.key == pygame.K_UP or event.key == ord('w'):
                newPosY = -5
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                newPosY = 5
                
        if event.type == pygame.KEYUP:
            if event.key == ord('w') or event.key == ord('s'):
                newPosY = 0
            if event.key == ord('a') or event.key == ord('d'):
                newPosX = 0

        #Potential Hitboxes
        playerHitbox = playerImg.get_rect(center=(objPosX, objPosY)) 
        objHitbox = objImg.get_rect(center=(objPosX, objPosY))
        # if playerHitbox.colliderect(objHitbox):
        #     print("lol")
        
        
        
        if lives == 0:
        #PRINTS GAMEOVER OR SOMETHING IDK
            screen.fill((555,555,555))
            # gameOver = pygame.image.load('GameOver.png')
 
        
        


    #BOUNDARIES
    #Position X goes off WIDTH (+100)
    #Position Y goes off HEIGHT (-100)
    if posX > 700:
        posX = 700
    if posX < 0:
        posX = 0
    if posY < 500:
        posY = 500
    if posY < 0:
        posY = 0
    


    posX = posX + newPosX
    posY = posY + newPosY
    player()
    # objects()
    # objPosY = objPosY + objSpeed
    pygame.display.update()