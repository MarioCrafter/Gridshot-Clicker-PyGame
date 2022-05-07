import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,800))

running = True
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)

background = BLACK
key_dict = {}

rect = ball.get_rect()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_1:
                background = GREEN
            elif event.key == pygame.K_2:
                background = BLUE

    screen.fill(background)
    pygame.display.update()


pygame.quit()