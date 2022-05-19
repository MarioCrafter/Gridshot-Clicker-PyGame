import pygame
import buttonClass
import textClass
from Colors import Colors
from panelClass import panelObject

class endPanel(panelObject):
    def __init__(self,screen,wWidth,wHeigth,gameIns) -> None:
        super().__init__(screen,wWidth,wHeigth)
        self.gameIns = gameIns
        self.screen = screen
        self.wWidth = wWidth
        self.wHeigth = wHeigth

        #Retry Button 
        self.retryBWidth = wWidth*0.07
        self.retryBHeigth = wHeigth*0.07
        self.retryBText = "RETRY"
        self.retryBXcord = wWidth//2 - self.retryBWidth//2
        self.retryBYcord = wHeigth//2-self.retryBHeigth//2
        self.retryBFontSize = int((self.retryBWidth*self.retryBHeigth) * 0.004) 

        self.retryButton = buttonClass.buttonObject(screen,
            self.retryBXcord,
            self.retryBYcord,
            Colors.ORANGE,
            Colors.WHITE,
            self.retryBWidth,
            self.retryBHeigth,
            self.font,
            self.retryBFontSize,
            "RETRY")

        #Retry Title
        self.retryTitleText = "Game Over"
        self.retryTitleFontSize = int(self.screenArea*0.00006)
        self.retryTitle = textClass.textObject(
            self.font,
            self.retryTitleFontSize,
            self.retryTitleText,
            Colors.WHITE)

    def render(self):
        self.screen.fill(self.background)
        self.retryButton.drawButton()
        self.retryTitle.drawText(
            self.screen,
            self.wWidth // 2 - self.retryTitle.getSize()[0] // 2,
            self.retryButton.y_coor - self.retryTitleFontSize+10)
        