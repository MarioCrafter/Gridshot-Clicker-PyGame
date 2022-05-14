from Colors import Colors
from panelClass import panelObject
import gameLogic
import buttonClass
import rectClass
import lineClass

class gamePanel(panelObject):
    def __init__(self,screen,wWidth,wHeight,gameIns) -> None:
        super().__init__(screen,wWidth,wHeight)
        self.gameIns = gameIns
        
        #Time Display 
        self.timeBWidth = wWidth*0.16
        self.timeBHeigth = wHeight*0.12
        self.timeBText = str(self.gameIns.time)
        self.timeBXcord = wWidth//2 - self.timeBWidth//2
        self.timeBYcord = 15
        self.timeBFontSize = int((self.timeBWidth*self.timeBHeigth) * 0.003)

        self.timeButton = buttonClass.buttonObject(
            screen,
            self.timeBXcord,
            self.timeBYcord,
            Colors.ORANGE,
            Colors.WHITE,
            self.timeBWidth,
            self.timeBHeigth,
            self.font,
            self.timeBFontSize,
            self.timeBText
        )
        
        #Point Display 
        self.pointBWidth = wWidth * 0.14
        self.pointBHeigth = wHeight * 0.09
        self.pointBText = str(self.gameIns.points) + " pts"
        self.pointBXcord = self.timeBXcord - self.pointBWidth + 1
        self.pointBYcord = self.timeBYcord + (self.timeBWidth//2 - self.pointBWidth//2)
        self.pointBFontSize = int((self.pointBWidth*self.pointBHeigth) * 0.003)

        self.pointButton = buttonClass.buttonObject(
            screen,
            self.pointBXcord,
            self.pointBYcord,
            Colors.ORANGE,
            Colors.WHITE,
            self.pointBWidth,
            self.pointBHeigth,
            self.font,
            self.pointBFontSize,
            self.pointBText
        )

        #Accuracy Display
        self.accBWidth = self.pointBWidth
        self.accBHeigth = self.pointBHeigth
        self.accBText = str(self.gameIns.accuracy) + "%"
        self.accBXcord = self.timeBXcord + self.timeBWidth
        self.accBYcord = self.pointBYcord
        self.accBFontSize = int((self.accBWidth*self.accBHeigth) * 0.003)

        self.accButton = buttonClass.buttonObject(
            screen,
            self.accBXcord,
            self.accBYcord,
            Colors.ORANGE,
            Colors.WHITE,
            self.accBWidth,
            self.accBHeigth,
            self.font,
            self.accBFontSize,
            self.accBText
        )
        
        #Speed Meter 
        self.sMBaseXcord = 60 
        self.sMBaseYcord = wHeight - 60  
        self.sMTopXcord = self.sMBaseXcord
        self.sMMaxY = (wWidth*(10/24))
        self.sMTopYcord = self.sMBaseYcord - self.sMMaxY + (self.sMMaxY//6 * self.gameIns.speed)
        self.sMWidth = int(wWidth*0.05)
        self.speedMeter = lineClass.lineObject(
            screen,
            self.sMBaseXcord,
            self.sMBaseYcord,
            self.sMTopXcord,
            self.sMTopYcord,
            Colors.ORANGE,
            self.sMWidth
        )

    def render(self):
        self.screen.fill(self.background)
        self.timeButton.drawButton()
        self.pointButton.drawButton()
        self.accButton.drawButton()
        self.speedMeter.drawLine()
