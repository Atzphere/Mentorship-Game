import sys
import pygame
from pygame import *
from random import randint

def startGame():
    
    color_black = (0, 0, 0)
    posX = 0 
    posY = 0

    speedX = 1
    speedY = 1
    
    pygame.init()
    winSize = (500, 500)
    screen = pygame.display.set_mode(winSize)
    pygame.display.set_caption("Load Image")

    ballIMG = pygame.image.load("Resources/ball.png")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        posX = posX + speedX
        posY = posY + speedY

        if (posX < 0) or (posX > 500) :
            speedX = - speedX
        if (posY < 0) or (posY> 500) :
            speedY = - speedY
        if randint(1, 500) == 1:
            speedY = randint(-1, 1)
            speedX = randint(-1, 1)
        screen.fill(color_black)
        screen.blit(ballIMG, (posX, posY))
        pygame.display.update()

startGame()
