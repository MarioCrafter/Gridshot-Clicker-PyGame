import pygame
from pygame.locals import *

class textObject:
    def __init__(self,font,size,text,color):
        self.font = pygame.font.SysFont(font,size)
        self.text = text
        self.color = color

    def drawText(self,screen,x_coord,y_coord):
        """
        Render and append text to screen
        """
        renderedText = self.font.render(self.text,True,self.color)
        screen.blit(renderedText, (x_coord,y_coord))

    def setColor(self, color):
        """
        Change Text Color 
        """
        self.color = color
        self.drawText()

    def getSize(self):
        return self.font.size(self.text)