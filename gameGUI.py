import pygame
import pygame,os
from pygame.locals import *
from .startPanel import startPanel
from .gamePanel import gamePanel
from .endPanel import endPanel

class gameGUI:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        info = pygame.display.Info()
        s_width,s_height = info.current_w, info.current_h
        w_width,w_height = s_width-10,s_height-50
        self.window = pygame.display.set_mode((w_width,w_height))
        self.eventMode = "START"
        self.changePanel(self.eventMode)

    def changePanel(self, panelName):
        """
        Change panel to panelName {START,GAME,END}
        """
        match panelName:
            case "START":
                screen = startPanel(self.window)
            case "GAME":
                screen = gamePanel(self.window)
            case "END":
                screen = endPanel(self.window)

    def screenLoop(self):
        while self.running:
            for event in pygame.event.get():
                match self.eventMode:
                    case "START":
                        self.startChecks(event)
                    case "GAME":
                        self.gameChecks(event)
                    case "END":
                        self.endChecks(event)

                
    #def startChecks(self,event):

    #def gameChecks(self,event):

    #def endChecks(self,event):