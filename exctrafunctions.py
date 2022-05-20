from ctypes import Array
import pygame
from objects_elements import *
import os
from time_elements import deltatime

#Load texture
def texture(name:str,scale:Array):
    texture=pygame.transform.scale(pygame.image.load(os.path.join('Assets',name+'.png')),(scale[0],scale[1]))
    return texture

#The start function
def start():
    '''create de frame'''
    frame = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("juego")

    '''create the game elements'''

    #background
    background = Object()
    background.setvar(0,0,texture('background',[1280,720]),0,0)

    #player
    player = Subject()
    player.setvar(640-60,300,texture('player',[120,120]),120,120)

    #bullet
    bullet = Bullet()
    bullet.setvar(280,0,texture('player',[720,720]),720,720)
    bullet.visible()

    #enemy
    enemy = Subject()
    enemy.setvar(640-60,300,texture('player',[120,120]),120,120)

    #deltatime
    dt = deltatime()

    #set the pool of objects
    objects = [background,bullet,enemy]

    return {'frame':frame,'player':player,'dt':dt,'objects':objects}