from polygon import Polygon

class Rectangle(Polygon):
    def __init__(self, eni, buyi): 
        super().__init__(eni, buyi ) 
        self.eni=eni 
        self.buyi=buyi 


    def yusi(self):
        return self.eni * self.buyi
    

    def piremetir(self):
        return 2*(self.eni +self.buyi)
