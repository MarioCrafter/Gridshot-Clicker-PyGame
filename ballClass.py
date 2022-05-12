import pygame
from pygame.locals import * 
import gameObjectClass

class ballObject(gameObjectClass):
    def __init__(self, surface, x_coor, y_coor, color):
        super().__init__(surface, x_coor, y_coor, color)()