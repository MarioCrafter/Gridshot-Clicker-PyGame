import pygame
from pygame.locals import *

class startPanel: 
    CYAN = (96, 168, 181)
    RED = (255,0,0)
    BLUE = (0,0,255)

    def __init__(self, screen):
        self.running = True
        self.background = self.BLUE
        self.screen = screen
        self.screen.fill(self.background)
        pygame.display.update()
        
        self.screenLoop()

    def screenLoop(self):
        while self.running: 
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.background = self.RED
                if event.type == pygame.MOUSEBUTTONUP:
                    self.background = self.CYAN
                
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill(self.background)

