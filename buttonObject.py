from .rectObject import rectObject
from .textClass import textClass

class buttonObject: 
    def __init__(self,surface,x_coor,y_coor,color,width,heigth,font,size,text):
        self.buttonBlock = rectObject(surface,x_coor,y_coor,color,width,heigth)
        self.buttonText = textClass(font,size,text,color)

        self.buttonBlock.drawRectangle()
        self.buttonText.drawText(surface,x_coor - width/2,y_coor)

