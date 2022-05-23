import array
import pygame
from objects_elements import *
import os
import time_elements

#Load texture
def texture(name:str,scale:array,rotate:int):
    texture=pygame.transform.scale(pygame.image.load(os.path.join('Assets',name+'.png')),(scale[0],scale[1]))
    texture=pygame.transform.rotate(texture,rotate)
    return texture

#The start function
def start():
    '''create de frame'''
    frame = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("juego")

    '''create the game elements'''
    #background
    background = Object()
    background.setvar(0,0,texture('background',[1280,720],0),0,0)

    #Pause
    pause = Object()
    pause.setvar(0,0,texture('pause',[1280,720],0),0,0)

    #player
    player = Subject()
    player.setvar(580,300,texture('player',[120,120],0),120,120)
    player.velocity = 200

    #bullet
    bullets = []
    for bullet in range(10):
        bullet = Bullet()
        bullet.setvar(280,0,texture('player',[120,120],0),120,120)
        bullet.visible()
        bullets.append(bullet)

    #enemy
    enemies = []
    for enemy in range(1):
        enemy = Subject()
        enemy.setvar(580,300,texture('player',[120,120],180),120,120)
        enemies.append(enemy)

    #deltatime
    dt = time_elements.Deltatime()

    return {'frame':frame,'player':player,'dt':dt,'bullets':bullets,'background':background,'enemies':enemies,'pause':pause}

def mpstart (array):
    pass