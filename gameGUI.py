import pygame
from pygame.locals import *
from startPanel import startPanel

class gameGUI: 
    pygame.init()
    screen = pygame.display.set_mode((1280,720),)
    sPanel = startPanel(screen)