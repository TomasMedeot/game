#primary class for objects
import array
import threading
import time_elements


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
        self.xhit = [self.xposition - self.margin_wide, self.xposition + self.margin_wide]
        self.yhit = [self.yposition - self.margin_high, self.yposition + self.margin_high]
        return [self.xhit,self.yhit]
        
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
        self.velocity = 150
        self.shooted = False

    def shoot(self):
        self.shooted = True
        self.visible()

    def deactivate(self):
        self.shooted = False
        self.visible()

    def hit(self,player:object,deltatime:float):
        if self.shooted == True:
            self.player_hit = player.gethitbox()
            self.player_x_hit = self.player_hit[0]
            self.player_y_hit = self.player_hit[1]
            if self.player_x_hit[0] < self.xposition < self.player_x_hit[1] and self.player_y_hit[0] < self.yposition < self.player_y_hit[1]:
                player.life = player.life - 50
                self.deactivate()
            else:
                if self.yposition >= 720:
                    self.deactivate()
                else:
                    self.move(0,self.velocity*deltatime)
            
#Class for de subjects(npc and player)
class Subject (Object):
    #Set the principals variables
    def __init__(self):
        self.life = 100
        self.velocity = 50
        self.direction = 1
        self.left = False
        self.right = False
        self.delay = True
        self.next_shoot = None

    #Continue player moving
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
                self.move(-self.velocity*deltatime,0)
        if self.right == True:
            if self.xposition <= 1220:
                self.move(self.velocity*deltatime,0)

    #Delay in AI shoot
    def whait(self):
        time_elements.time.sleep(2)
        self.delay=True

    #Fuction for Arificial Intelligence
    def AI (self,deltatime:float,player:object,bullets:array):

        #Set direction and move
        if self.show == True:
            if self.xposition <= 1220 and self.xposition >= -60:
                if self.direction == 1:
                    self.move(self.velocity*deltatime,0)
                elif self.direction == 0:
                    self.move(-self.velocity*deltatime,0)
            elif self.xposition >= 1220:
                self.direction = 0
                self.move(0,30)
                self.xposition = 1220
            elif self.xposition <= -60:
                self.direction = 1
                self.move(0,30)
                self.xposition = -60

        #Take an unused bullet
        if self.next_shoot == None:
            for bullet in bullets:
                if bullet.show == False:
                    self.next_shoot = bullet
                    break
        #shoot
        if (player.xposition-5)<self.xposition<(player.xposition+5) and self.delay == True:
            self.delay = False
            self.next_shoot.setposition(self.xposition,self.yposition)
            self.next_shoot.shoot()
            self.t1=threading.Thread(target=self.whait)
            self.t1.start()
            self.next_shoot = None