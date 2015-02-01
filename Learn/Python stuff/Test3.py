import sys
import pygame
from pygame.locals import *

keys = [False, False, False, False]
pos = [100, 100]

pygame.init()

def loadImage(pic_name):
    return pygame.image.load("Resources/" + pic_name)


def controlBall(event):
    speed = [x, y] = [0, 0]
    speedOffSet = 2

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            keys[0] = True
        if event.key == pygame.K_RIGHT:
            keys[1] = True
        if event.key == pygame.K_UP:
            keys[2] = True
        if event.key == pygame.K_DOWN:
            keys[3] = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            keys[0] = False
        if event.key == pygame.K_RIGHT:
            keys[1] = False
        if event.key == pygame.K_UP:
            keys[2] = False
        if event.key == pygame.K_DOWN:
            keys[3] = False

    if keys[0]:
        pos[0] -= speedOffSet
    elif keys[1]:
        pos[0] += speedOffSet
    if keys[2]:
        pos[1] -= speedOffSet
    if keys[3]:
        pos[1] += speedOffSet
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
        screen.fill(color_black)
        fps_clock.tick(fps)
        pygame.display.set_caption(str(fps_clock.get_fps()))
        screen.blit(ballIMG, pos)
        pygame.display.update()

playBall()

        
