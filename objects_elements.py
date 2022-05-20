#primary class for objects
class Object:
    def __init__(self):
        self.texture = ''
        self.xposition = 0
        self.yposition = 0
        self.show = True 

    #Set the basic variables for the objects
    def setvar (self,xposition:int,yposition:int,texture,wide:int,high:int):
        self.texture = texture
        self.xposition = xposition
        self.yposition = yposition
        self.margin_wide = wide/2
        self.margin_high = high/2
        self.show = True

    #Set the hit box for colitions
    def gethitbox (self):
        self.xhit = self.xposition + self.margin_wide
        self.yhit = self.yposition + self.margin_high
        
    #Move the object to the cordenades 
    def setposition(self,xposition:int,yposition:int):
        self.xposition = xposition
        self.yposition = yposition

    #Move the object whith number on x/y
    def move(self,xmove:float,ymove:float):
        self.xposition = self.xposition + xmove
        self.yposition = self.yposition + ymove

    #Invert variable of if draw or not
    def visible(self):
        if self.show == True:
            self.show = False
        elif self.show == False:
            self.show = True

    #Draw on the window
    def draw(self,frame:object):
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

    def hit(self,player:object,deltatime:float):
        if self.shooted == True:
            if not self.xposition == player.xposition and self.yposition == player.yposition:
                self.move(0,-10*deltatime)
            else:
                player.life = player.life - 10
                self.deactivate()

#Class for de subjects(npc and player)
class Subject (Object):
    #Set the principals variables
    def __init__(self):
        self.life = 100
        self.velocity = 10
        self.jump = 1
        self.amunation = 20
        self.direction = 1
        self.left = False
        self.right = False

    def cont_move(self,key:str,status:bool):
        if key == 'a':
            if status == True:
                self.left = True
            else:
                self.left = False
        elif key == 'd':
            if status == True:
                self.right = True
            else:
                self.right = False

    #Move with key board comand and deltatime 
    def keymove(self,deltatime:float):
        if self.left == True:
            if self.xposition >= -60:
                self.move(-5*deltatime,0)
        if self.right == True:
            if self.xposition <= 1220:
                self.move(5*deltatime,0)
    
    #Set the bullet to shoot 
    def shoot (self,bullet:object):
        bullet.setposition(self.xposition,self.yposition)
        bullet.visible()
        bullet.shoot()

    #Fuction for Arificial Intelligence
    def AI (self,player:object,bullet:object,deltatime:float):
        '''set direction and move'''
        if self.show == True:
            if self.xposition <= 1220 and self.xposition >= -60:
                if self.direction == 1:
                    self.move(self.velocity*deltatime,0)
                elif self.direction == 0:
                    self.move(-self.velocity*deltatime,0)
            elif self.xposition >= 1220:
                self.direction = 0
                self.move(0,30*deltatime)
                self.xposition = 1220
            elif self.xposition <= -60:
                self.direction = 1
                self.move(0,30*deltatime)
                self.xposition = -60

        '''if enemy.xposition == self.xposition:
            self.shoot(bullet)'''