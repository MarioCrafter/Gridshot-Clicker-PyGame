import rectClass
import textClass
class buttonObject: 
    def __init__(self,surface,x_coor,y_coor,rectColor,textColor,width,heigth,font,size,text):
        self.buttonBlock = rectClass.rectObject(surface,x_coor,y_coor,rectColor,width,heigth)
        self.buttonText = textClass.textObject(font,size,text,textColor)
        self.surface = surface
        self.width = width 
        self.heigth = heigth
        self.x_coor = x_coor
        self.y_coor = y_coor


    def drawButton(self):
        self.buttonBlock.drawRectangle()
        self.buttonText.drawText(self.surface,self.x_coor + self.width//5,self.y_coor + self.heigth//4)


