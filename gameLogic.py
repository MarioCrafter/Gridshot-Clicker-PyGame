class gameLogic:
    def __init__(self) -> None:
        self.points = 0
        self.time = 0
        # 0% <= accuracy <= 100%
        self.accuracy = 0.0
        #1 <= speed <= 6 
        self.speed = 1