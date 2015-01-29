import sys
import pygame
from pygame.locals import *
def start():

    color_blue = (00,155,120)
    
    pygame.init()
    WindowSize = (Width, Height) = (500, 500)
    screen = pygame.display.set_mode(WindowSize, pygame.RESIZABLE)
    pygame.display.set_caption("First Window!")
    
    while True:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                pygame.quit()
                sys.exit()
        
        screen.fill(color_blue)        
        pygame.display.update()

if __name__ == '__main__':
    start()
