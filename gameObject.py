import pygame
from pygame.locals import *

class gameObject:
    def __init__(self, surface, x_coor, y_coor,color): 
        self.displayVar = surface
        self.x_coordinate = x_coor
        self.y_coordinate = y_coor
        self.color = color
        self.coordinates = [self.x_coordinate,self.y_coordinate]
    
    def getXcoord(self): 
        return self.x_coordinate

    def getYcoord(self):
        return self.y_coordinate

    def getColor(self):
        return self.color
    
    def getCoordinates(self):
        return self.coordinates

    def setXcoordinate(self,num):
        self.x_coordinate = num
    
    def setYcoordinate(self,num):
        self.y_coordinate = num
    
    def setColor(self,col):
        self.color = col
