import sys
import pygame
from pygame.locals import *

pygame.init()

def loadImage(pic_name):
    return pygame.image.load("Resources/" + pic_name)


def controlBall(event):
    speed = [x, y] = [0, 0]
    speedOffSet = 16

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            speed[0] = -speedOffSet
        if event.key == pygame.K_RIGHT:
            speed[0] = speedOffSet
        if event.key == pygame.K_UP:
            speed[1] = -speedOffSet
        if event.key == pygame.K_DOWN:
            speed[1] = speedOffSet

    if event.type in (pygame.KEYUP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
        speed = [0, 0]
    return speed



def playBall():
    winSize =(width, height) = (680, 480)
    screen = pygame.display.set_mode(winSize)
    color_black = (0,0,0)
    pygame.display.set_caption("controlBall")

    ballIMG = loadImage("ball.png")
    fps = 30
    fps_clock = pygame.time.Clock()

    posX = 0
    posY = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit
                sys.exit()
        curSpeed = controlBall(event)
        posX += curSpeed[0]
        posY += curSpeed[1]
        screen.fill(color_black)
        fps_clock.tick(fps)
        pygame.display.set_caption(str(fps_clock.get_fps()))
        screen.blit(ballIMG, (posX, posY))
        pygame.display.update()

playBall()

        
