from turtle import width
import pygame
from pygame.locals import * 
from gameObjectClass import gameObject

class ballObject(gameObject):
    def __init__(self, surface, x_coor, y_coor, color, radius):
        super().__init__(surface, x_coor, y_coor, color)
        self.radius = radius

    def drawCircle(self):
        '''
        Render circle object
        '''
        pygame.draw.circle(self.displayVar,self.color,self.y_coordinate,self.x_coordinate,self.radius)

    def setRadius(self,radius):
        '''
        Set int circle radius
        '''
        self.radius = radius