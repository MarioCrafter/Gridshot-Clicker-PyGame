from asyncio.windows_events import NULL
import pygame
import pygame,os
from pygame.locals import *
from Colors import Colors
import startPanel
import gamePanel
import endPanel
import gameLogic

class gameGUI:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        info = pygame.display.Info()
        s_width,s_height = info.current_w, info.current_h
        self.w_width,self.w_height = s_width-10,s_height-50
        self.window = pygame.display.set_mode((self.w_width,self.w_height))
        pygame.display.set_caption("Gridshot Clicker")
        self.eventMode = "START"
        self.changePanel(self.eventMode)
        self.screenLoop()

    def changePanel(self, panelName):
        """
        Change panel to panelName {START,GAME,END}
        """
        match panelName:
            case "START":
                self.screen = NULL
                self.screen = startPanel.startPanel(self.window,self.w_width,self.w_height)
            case "GAME":
                self.screen = NULL
                self.eventMode = "GAME"
                self.gameIns = gameLogic.gameLogic()
                self.screen = gamePanel.gamePanel(self.window,self.w_width,self.w_height,self.gameIns)
            case "END":
                self.screen = endPanel.endPanel(self.window)

    def screenLoop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                match self.eventMode:
                    case "START":
                        self.screen.render()
                        self.startChecks(event)
                    case "GAME":
                        self.screen.render()
                        #self.gameChecks(event)
                '''
                    case "END":
                        self.endChecks(event)
                '''
                pygame.display.update()


    def mouseOver(self,xInit,xFinal,yInit,yFinal):
        mousePos = pygame.mouse.get_pos()
        if xInit <= mousePos[0] <= xFinal and yInit <= mousePos[1] <= yFinal:
            return True
        return False


    def startChecks(self,event):
        if self.mouseOver(
                self.screen.startBXcord,
                self.screen.startBXcord + self.screen.startBWidth,
                self.screen.startBYcord,
                self.screen.startBYcord + self.screen.startBHeigth):

            self.screen.startButton.buttonBlock.setColor(Colors.RED)

        else:
            self.screen.startButton.buttonBlock.setColor(Colors.ORANGE)   

        if event.type == MOUSEBUTTONDOWN:
            if self.mouseOver(
                    self.screen.startBXcord,
                    self.screen.startBXcord + self.screen.startBWidth,
                    self.screen.startBYcord,
                    self.screen.startBYcord + self.screen.startBHeigth):
                    
                self.changePanel("GAME")


    #def gameChecks(self,event):

    #def endChecks(self,event):