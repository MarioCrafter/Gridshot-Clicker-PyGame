import pygame
from Colors import Colors
from pygame.locals import *
import buttonClass
import textClass


class startPanel(): 
    def __init__(self, screen, wWidth, wHeigth):
        self.screen = screen
        self.background = Colors.GOLD
        self.font = "Bernard MT"
        self.screenArea = wWidth*wHeigth
        self.wWidth = wWidth
        self.wHeigth = wHeigth

        #Start Button
        self.startButtonWidth = wWidth*0.07
        self.startButtonHeigth = wHeigth*0.07
        self.startButtonText = "START"
        self.startButtonXcord = wWidth//2-self.startButtonWidth//2
        self.startButtonYcord = wHeigth//2-self.startButtonHeigth//2
        self.startBFontSize = int((self.startButtonWidth+self.startButtonHeigth)//(len(self.startButtonText)))
        self.startButton = buttonClass.buttonObject(screen,self.startButtonXcord,self.startButtonYcord,Colors.ORANGE,Colors.WHITE,self.startButtonWidth,self.startButtonHeigth,self.font,self.startBFontSize,"START")

        #Start Title
        self.startTitleText = "Gridshot Circle Clicker"
        self.startTitleFontSize = int(self.screenArea*0.00006)
        self.startTitle = textClass.textObject(self.font,self.startTitleFontSize,self.startTitleText,Colors.WHITE)


    def render(self):
        self.screen.fill(self.background)
        self.startButton.drawButton()     
        self.startTitle.drawText(self.screen,self.wWidth//4,self.startButtonYcord-self.startTitleFontSize+10)



