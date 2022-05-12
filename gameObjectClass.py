import pygame
from pygame.locals import *

class gameObject:
    def __init__(self, surface, x_coor, y_coor,color): 
        self.displayVar = surface
        self.x_coordinate = x_coor
        self.y_coordinate = y_coor
        self.color = color
    
    def getXcoord(self): 
        """
        return int x-coordinate
        """
        return self.x_coordinate

    def getYcoord(self):
        """
        return int y-coordinate
        """
        return self.y_coordinate

    def getColor(self):
        """
        return tuple color
        """
        return self.color

    def setXcoordinate(self,num):
        """
        set int x-coordinate
        """
        self.x_coordinate = num
    
    def setYcoordinate(self,num):
        """
        set int y-coordinate
        """
        self.y_coordinate = num
    
    def setColor(self,col):
        """
        set tuple color
        """
        self.color = col
