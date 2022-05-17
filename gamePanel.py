from Colors import Colors
from ballClass import ballObject
from panelClass import panelObject
import gameLogic
import buttonClass
import rectClass
import lineClass
import ballClass

class gamePanel(panelObject):
    def __init__(self,screen,wWidth,wHeigth,gameIns) -> None:
        super().__init__(screen,wWidth,wHeigth)
        self.gameIns = gameIns
        self.screen = screen
        self.wWidth = wWidth
        self.wHeigth = wHeigth

        #Time Display 
        self.timeBWidth = wWidth*0.16
        self.timeBHeigth = wHeigth*0.12
        self.timeBText = str(self.gameIns.time) + " s"
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
        self.pointBHeigth = wHeigth * 0.09
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
        self.sMBaseYcord = wHeigth - 60  
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

        #Orb Constants
        self.radius = int((self.wWidth*self.wHeigth)*0.000024)
        self.orbColor = Colors.RED

    def makeGameElements(self):
        #Orb Objects
        self.orbList = []
        self.generateOrb()
        self.generateOrb()
        self.generateOrb()

    def generateOrb(self):
        x,y = self.gameIns.generateCoordinate()
        orb = ballClass.ballObject(self.screen,x,y,self.orbColor,self.radius)
        self.orbList.append(orb)
        return orb

    def deleteOrb(self,pos):
        for orb in self.orbList:
            if orb.coords == pos: 
                self.orbList.remove(orb)
        self.generateOrb()    


    def render(self,gameIns):
        self.screen.fill(self.background)
        self.timeButton.buttonText.text = str(gameIns.time) + " s"
        self.timeButton.drawButton()
        self.pointButton.buttonText.text = self.pointBText = str(self.gameIns.points) + " pts"
        self.pointButton.drawButton()
        self.accButton.buttonText.text = str(gameIns.accuracy) + "%"
        self.accButton.drawButton()
        self.speedMeter.y2 = self.sMBaseYcord - self.sMMaxY + (self.sMMaxY//6 * gameIns.speed)
        self.speedMeter.drawLine()

        for orb in self.orbList:
            orb.drawCircle()

