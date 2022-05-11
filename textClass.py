import pygame
from pygame.locals import *

class textClass:
    def __init__(self, font,size,text,color):
        self.font - pygame.font.SysFont(font,size)
        self.text = text
        self.color = color

    def drawText(self,screen,x_coord,y_coord):
        renderedText = self.font.render(self.text,True,self.color)
        screen.blit(renderedText, (x_coord,y_coord))
