import sys
import pygame
from random import randint
from pygame.locals import *
def start():

    color_blue = (00,155,120)
    color_red = (155, 00, 00)
    pygame.init()
    WindowSize = (Width, Height) = (500, 500)
    screen = pygame.display.set_mode(WindowSize, pygame.RESIZABLE)
    pygame.display.set_caption("First Window!")
    
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                color_red = (randint(1, 155), randint(1, 155), randint(1,155))
                Rect_Data = Rect(x,y,randint(1, 150),randint(1, 150))
                #creates rectangle at x,y width = 100 height = 100
                pygame.draw.rect(screen, color_red, Rect_Data)
                print (red_color)
            if event.type in (QUIT, KEYDOWN):
                pygame.quit()
                sys.exit()
        
        #screen.fill(color_blue)        
        pygame.display.update()

def start2():

    color_blue = (00,155,120)
    color_red = (155, 00, 00)
    pygame.init()
    WindowSize = (Width, Height) = (500, 500)
    screen = pygame.display.set_mode(WindowSize, pygame.RESIZABLE)
    pygame.display.set_caption("First Window!")
    
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                color_red = (randint(1, 155), randint(1, 155), randint(1,155))
                pygame.draw.circle(screen, color_red, (x,y), randint(1, 90), 0)
            if event.type in (QUIT, KEYDOWN):
                pygame.quit()
                sys.exit()
        
        #screen.fill(color_blue)        
        pygame.display.update()
while True:
    response = input("Circles or rectangles? ")
    if response == 'rectangles':
        start()
        break
    elif response == "circles":
        start2()
        break
    else:
        print("INVALID:")
