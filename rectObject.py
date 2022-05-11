import pygame
from pygame.locals import *
class rectObject(gameObject):
    def __init__(self,surface,x_coor,y_coor,color,width,heigth):
        super().__init__(surface,x_coor,y_coor,color)
        self.width = width
        self.height = heigh
    
    def drawRectangle(self):
        pygame.draw.rect(self.surface,self.color,[
            self.x_coordinate,
            self.y_coordinate,
            self.width,
            self.heigth
        ])

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height


