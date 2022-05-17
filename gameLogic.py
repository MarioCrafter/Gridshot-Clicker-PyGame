from asyncio.windows_events import NULL
from random import randint
import gamePanel
class gameLogic:
    def __init__(self,wWdith,wHeight) -> None:
        self.wWidth = wWdith
        self.wHeigth = wHeight
        self.points = 0
        self.time = 60
        # 0% <= accuracy <= 100%
        self.accuracy = 100.0
        #1 <= speed <= 6 
        self.speed = 1
        self.gameEnvironmentCheck = 0

    def getPanel(self, gamePanel):
        self.gamePanel = gamePanel
        self.gameEnvironment()
    
    def gameEnvironment(self):
        self.topBound = int(self.gamePanel.timeBYcord + 10 + self.gamePanel.timeBWidth)
        self.bottonBound = int(self.wHeigth - 30)
        self.yDistance = self.bottonBound - self.topBound
        self.leftBound = int(self.gamePanel.sMBaseXcord + self.gamePanel.sMWidth*2)
        self.rightBound = int(self.wWidth - self.leftBound)
        self.xDistance = self.rightBound - self.leftBound
        self.gameGrid = self.coordinateGrid()
        self.orbPositions = []
        self.gamePanel.makeGameElements()

    def coordinateGrid(self):
        #Divisions = Len of side / (2*radius + Circle Gap)
        xDivisons = int((self.xDistance)//(2*self.gamePanel.radius + 2))
        yDivisions = int((self.yDistance)//(2*self.gamePanel.radius + 2))
        grid = []
        for x in range(self.leftBound + self.gamePanel.radius,self.rightBound - self.gamePanel.radius+1,self.xDistance//xDivisons):
            for y in range(self.topBound + self.gamePanel.radius,self.bottonBound - self.gamePanel.radius+1,self.yDistance//yDivisions):
                grid.append([x,y])
        return grid

    def checkCoordinate(self,coord):
        if self.orbPositions == NULL:
            return False
        elif coord in self.orbPositions:
            return True
        return False
    
    def generateCoordinate(self):
        randIndex = randint(0,len(self.gameGrid)-1)
        newCoord = self.gameGrid[randIndex]
        while self.checkCoordinate(newCoord):
            randIndex = randint(0,len(self.gameGrid)-1)
            newCoord = self.gameGrid[randIndex] 
        self.orbPositions.append(newCoord) 
        return newCoord  

    def removeOrb(self,pos):
        for coord in self.orbPositions:
            if coord == pos:
                self.orbPositions.remove(coord)
        self.gamePanel.deleteOrb(pos)

