import time

#primary class for objects
class Object:
    def __init__(self):
        self.texture = ''
        self.xposition = 0
        self.yposition = 0
        self.show = True 

    def setvar (self,xposition,yposition,texture,wide,high):
        self.texture = texture
        self.xposition = xposition
        self.yposition = yposition
        self.margin_wide = wide/2
        self.margin_high = high/2
        self.show = True

    def gethitbox (self):
        self.xhit = self.xposition + self.margin_wide
        self.yhit = self.yposition + self.margin_high
        
    def setposition(self,xposition,yposition):
        self.xposition = xposition
        self.yposition = yposition

    def move(self,xmove,ymove):
        self.xposition = self.xposition + xmove
        self.yposition = self.yposition + ymove

    def visible(self):
        if self.show == True:
            self.show = False
        elif self.show == False:
            self.show = True

    def draw(self,frame):
        if self.show == True:
            frame.blit(self.texture,(self.xposition,self.yposition))


#bullet class
class Bullet (Object):
    def __init__(self):
        self.velocity = 1
        self.shooted = False

    def shoot(self):
        self.shooted = True

    def deactivate(self):
        if self.yposition == 0:
            self.shooted = False
            self.visible()

    def hit(self,player,deltatime):
        if self.shooted == True:
            if not self.xposition == player.xposition and self.yposition == player.yposition:
                self.move(0,-10*deltatime)
            else:
                player.life = player.life - 10
                self.deactivate()

#Class for de subjects(npc and player)
class Subject (Object):
    def __init__(self):
        self.life = 100
        self.velocity = 1
        self.jump = 1
        self.amunation = 20
        self.direction = 1

    def keymove(self,deltatime,key):
        if key == 'a':
            if self.xposition <= 1920:
                self.move(-1*deltatime,0)
        elif key == 'd':
            if self.xposition >= 0:
                self.move(1*deltatime,0)
       
    def shoot (self,bullet):
        bullet.setposition(self.xposition,self.yposition)
        bullet.visible()
        bullet.shoot()

    def AI (self,player,bullet,deltatime):
        '''set direction and move'''
        if self.show == True:
            if self.xposition == 1920:
                self.direction = 1
                self.move(0,1*deltatime)
            elif self.xposition == 0:
                self.direction = 0
                self.move(0,-1*deltatime)

            if self.direction == 1:
                self.move(10*deltatime,0)
            elif self.direction == 0:
                self.move(-10*deltatime,0)

        '''if enemy.xposition == self.xposition:
            self.shoot(bullet)'''

'''delta time class'''
class deltatime():
    def __init__(self):
        self.mili_seconds = 0
        self.prev = 0
        self.actual = 0
        self.deltatime = 0

    def refresh(self):
        self.actual = self.actual + 1
        return self.deltatime
    
    def calc_dt(self):
        while True:
            print(self.mili_seconds)
            if str(self.actual) == str(self.prev):
                print('a')
                self.mili_seconds = self.mili_seconds + 1
                self.prev = self.actual
            else:
                print('b')
                self.deltatime = 1/self.mili_seconds
                self.mili_seconds = 0
            time.sleep(0.1)
