import pygame
import buttonClass
import textClass
from Colors import Colors
from pygame.locals import *
from panelClass import panelObject



class startPanel(panelObject): 
    def __init__(self, screen, wWidth, wHeigth):
        super().__init__(screen,wWidth,wHeigth)

        #Start Button
        self.startBWidth = wWidth*0.07
        self.startBHeigth = wHeigth*0.07
        self.startBText = "START"
        self.startBXcord = wWidth//2-self.startBWidth//2
        self.startBYcord = wHeigth//2-self.startBHeigth//2
        self.startBFontSize = int((self.startBWidth*self.startBHeigth) * 0.004)
        
        self.startButton = buttonClass.buttonObject(screen,
            self.startBXcord,
            self.startBYcord,
            Colors.ORANGE,
            Colors.WHITE,
            self.startBWidth,
            self.startBHeigth,
            self.font,
            self.startBFontSize,
            "START")

        #Start Title
        self.startTitleText = "Gridshot Circle Clicker"
        self.startTitleFontSize = int(self.screenArea*0.00006)
        self.startTitle = textClass.textObject(
            self.font,
            self.startTitleFontSize,
            self.startTitleText,
            Colors.WHITE)
            
    def render(self):
        self.screen.fill(self.background)
        self.startButton.drawButton()     
        self.startTitle.drawText(
            self.screen,
            self.wWidth//4,
            self.startButton.y_coor-self.startTitleFontSize+10)



