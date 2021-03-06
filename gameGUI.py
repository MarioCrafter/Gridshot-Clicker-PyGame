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
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Gridshot Clicker")
        self.eventMode = "START"
        self.changePanel(self.eventMode)
        self.screenLoop()

    def changePanel(self, panelName):
        """
        Change panel to panelName {START,GAME,END}
        """
        #info = pygame.display.Info()
        #self.w_width,self.w_height = info.current_w, info.current_h
        match panelName:
            case "START":
                self.screen = NULL
                self.screen = startPanel.startPanel(self.window,self.w_width,self.w_height)
            case "GAME":
                self.screen = NULL
                self.eventMode = "GAME"
                self.gameIns = gameLogic.gameLogic(self.w_width,self.w_height)
                self.screen = gamePanel.gamePanel(self.window,self.w_width,self.w_height,self.gameIns)
                self.gameIns.getPanel(self.screen)
                pygame.time.set_timer(pygame.USEREVENT,1000)
            case "END":
                self.screen = NULL
                self.eventMode = "END"
                self.screen = endPanel.endPanel(self.window,self.w_width,self.w_height,self.gameIns)
                pygame.time.set_timer(pygame.USEREVENT,0)


    def screenLoop(self):
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                match self.eventMode:
                    case "START":
                        self.screen.render()
                        self.startChecks(event)
                    case "GAME":
                        self.gameIns.updateSpeed()
                        self.screen.render(self.gameIns)
                        self.gameChecks(event)
                    case "END":
                        self.screen.render()
                        self.endChecks(event)

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

    def gameChecks(self,event):
        if event.type == pygame.USEREVENT:
            if self.gameIns.time != -1: 
                self.gameIns.updateTime()
            if self.gameIns.time == -1: 
                self.changePanel("END")


        if event.type == MOUSEBUTTONDOWN and self.gameIns.time > 0:
            r = self.screen.radius
            x1 = self.gameIns.orbPositions[0][0]
            y1 = self.gameIns.orbPositions[0][1]
            x2 = self.gameIns.orbPositions[1][0]
            y2 = self.gameIns.orbPositions[1][1]
            x3 = self.gameIns.orbPositions[2][0]
            y3 = self.gameIns.orbPositions[2][1]
            
            if self.mouseOver(x1-r,x1+r,y1-r,y1+r):
                    self.gameIns.removeOrb([x1,y1])

            if self.mouseOver(x2-r,x2+r,y2-r,y2+r):
                    self.gameIns.removeOrb([x2,y2])

            if self.mouseOver(x3-r,x3+r,y3-r,y3+r):
                    self.gameIns.removeOrb([x3,y3])
                
            if not self.mouseOver(x1-r,x1+r,y1-r,y1+r):
                if not self.mouseOver(x2-r,x2+r,y2-r,y2+r):
                    if not self.mouseOver(x3-r,x3+r,y3-r,y3+r):
                        self.gameIns.misses += 1
                        self.gameIns.updateAccuracy()        

    
    def endChecks(self,event):
        if self.mouseOver(
                self.screen.retryBXcord,
                self.screen.retryBXcord + self.screen.retryBWidth,
                self.screen.retryBYcord,
                self.screen.retryBYcord + self.screen.retryBHeigth):

            self.screen.retryButton.buttonBlock.setColor(Colors.RED)
        else:
            self.screen.retryButton.buttonBlock.setColor(Colors.ORANGE)   

        if event.type == MOUSEBUTTONDOWN:
            if self.mouseOver(
                    self.screen.retryBXcord,
                    self.screen.retryBXcord + self.screen.retryBWidth,
                    self.screen.retryBYcord,
                    self.screen.retryBYcord + self.screen.retryBHeigth):
                    
                self.changePanel("GAME")     
        

