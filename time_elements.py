import time

#Deltatime pakage
class Deltatime():
    def __init(self):
        self.deltatime = 0
        self.prev = 0
        self.actual = 0
    
    def calc_dt (self):
        self.actual=time.time()
        self.deltatime= self.actual - self.prev 
        self.prev = self.actual
        return self.deltatime  