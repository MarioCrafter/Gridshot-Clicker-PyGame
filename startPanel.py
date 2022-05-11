import pygame
from .Colors import Colors
from pygame.locals import *

class startPanel: 
    def __init__(self, screen):
        self.background = Colors.GOLD
        screen.fill(self.background)

