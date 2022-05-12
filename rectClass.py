import pygame
from pygame.locals import *
from gameObjectClass import gameObject
class rectObject(gameObject):
    def __init__(self,surface,x_coor,y_coor,color,width,heigth):
        super().__init__(surface,x_coor,y_coor,color)
        self.surface = surface
        self.width = width
        self.heigth = heigth
    
    def drawRectangle(self):
        """
        Render rectangle object
        """
        pygame.draw.rect(self.surface,self.color,[
            self.x_coordinate,
            self.y_coordinate,
            self.width,
            self.heigth,
        ])

    def getWidth(self):
        """
        Returns int width of rectangle
        """
        return self.width
    
    def getHeight(self):
        """
        Return int height of rectangle
        """
        return self.height


