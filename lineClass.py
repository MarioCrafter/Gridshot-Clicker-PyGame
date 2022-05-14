import pygame 
from pygame.locals import * 
from Colors import Colors
class lineObject(): 
    def __init__(self,surface,x1_coor,y1_coor,x2_coor,y2_coor,color,width) -> None:
        self.surface = surface
        self.x1 = x1_coor
        self.y1 = y1_coor
        self.x2 = x2_coor
        self.y2 = y2_coor
        self.color = color 
        self.width = width
    
    def drawLine(self):
        '''
        Render line object
        '''
        pygame.draw.line(
            self.surface,
            self.color,
            (self.x1,self.y1),
            (self.x2,self.y2),
            self.width)