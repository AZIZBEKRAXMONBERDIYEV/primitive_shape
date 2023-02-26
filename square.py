from polygon import Polygon

class Square(Polygon):
    def __init__(self, uzunlik): 
        super().__init__(uzunlik ) 
        self.uzunlik=uzunlik

    def yusi(selt):
        return selt.uzunlik**2
    
    def premetir(self):
        return 4*self.uzunlik