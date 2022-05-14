from Colors import Colors
class panelObject: 
    def __init__(self,screen,wWidth,wHeigth) -> None:
        self.screen = screen
        self.wWidth = wWidth
        self.wHeigth = wHeigth
        self.font = "Bernard MT"
        self.background = Colors.GOLD
        self.screenArea = wWidth*wHeigth