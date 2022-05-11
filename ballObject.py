import pygame
from pygame.locals import * 
from gameObject import gameObject

class ballObject(gameObject):
    def __init__(self, surface, x_coor, y_coor, color):
        super().__init__(surface, x_coor, y_coor, color)()