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
                self.screen = endPanel.endPanel(self.window)

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
                        print(self.gameIns.speed)
                        self.screen.render(self.gameIns)
                        self.gameChecks(event)
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

    def gameChecks(self,event):
        if event.type == pygame.USEREVENT:
            if self.gameIns.time > 0: 
                self.gameIns.updateTime()


        if event.type == MOUSEBUTTONDOWN and self.gameIns.time > 0:
            for pos in self.gameIns.orbPositions:
                r = self.screen.radius
                x = pos[0]
                y = pos[1]
                if self.mouseOver(x-r,x+r,y-r,y+r):
                    self.gameIns.removeOrb(pos)
            if self.mouseOver(0,x-r-1,0,y-r-1) or self.mouseOver(x+r+1,self.w_width,y+r+1,self.w_height):
                self.gameIns.updateAccuracy()
                print(self.gameIns.misses)

            


    #def endChecks(self,event):