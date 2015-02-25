import sys
import pygame
import random
from pygame.locals import *

keys = [False, False, False, False]

pygame.init()
class ClassBalls:
    def __init__(self):
        #self.num_balls = num_balls
        self.pos = [random.randint(0, 680), random.randint(0, 480)]
        self.loadImage()
        print(self.pos)
    def loadImage(self, pic_name="ball.png"):
        self.image = pygame.image.load("Resources/" + pic_name)


    def controlBall(self, event):
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
                keys[0] = False
                keys[1] = False
                keys[2] = False
                keys[3] = False

        if keys[0]:
            self.pos[0] -= speedOffSet

        elif keys[1]:
            self.pos[0] += speedOffSet
        if keys[2]:
            self.pos[1] -= speedOffSet
        if keys[3]:
            self.pos[1] += speedOffSet
        return speed



def playBall():
    winSize =(width, height) = (680, 480)
    screen = pygame.display.set_mode(winSize)
    color_black = (0,0,0)
    pygame.display.set_caption("controlBall")

    fps = 30
    fps_clock = pygame.time.Clock()

    posX = 0
    posY = 0

    balls = []
    for c in range(1, 6):
        balls.append(ClassBalls())

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit
                sys.exit()

        if (event.type == pygame.KEYDOWN or event.type == pygame.KEYUP):
            screen.fill(color_black)
            fps_clock.tick(fps)
            pygame.display.set_caption(str(fps_clock.get_fps()))

            for ball in balls:
                ball.controlBall(event)
                screen.blit(ball.image, ball.pos)
                pygame.display.update()

if __name__ == "__main__":
    playBall()
