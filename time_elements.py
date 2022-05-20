import time

#Deltatime package
class deltatime():
    def __init__(self):
        self.run = True
        self.miliseconds = 0
        self.frame2 = 0
        self.frame = 0

    def prev(self):
        self.frame2 = self.frame

    def sum_miliseconds(self):
        self.miliseconds = self.miliseconds + 0.1
        self.sub = self.sub + 1
        time.sleep(0.001)

    def fp(self):
        self.sub = 0
        self.frame2 = 0
        self.miliseconds = 0

        while self.run == True:
            if self.frame == self.frame2:
                self.sum_miliseconds()
            else:
                print(self.miliseconds)
                self.miliseconds = 0
                self.prev()