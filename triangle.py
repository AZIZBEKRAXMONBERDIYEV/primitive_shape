from polygon import Polygon
from math import sqrt
class Triangle(Polygon):
    def __init__(self, a, b, c):
        
        self.a = a
        self.b = b
        self.c = c

    #uchburcha qoydasi
    def uchburchak(self):
        if self.a>self.b+self.c and self.b>self.a+self.c and self.c>self.b+self.b:
            return 'uchburchak'
        else:
            return 'uchburchakemas'
        
    def yuzi(self):
        p = (self.a + self.b + self.c) // 2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
    
    def premetiri(self):
        return self.a + self.b + self.c