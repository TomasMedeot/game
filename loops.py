import array
import threading
import pygame
import time_elements
import exctrafunctions
pygame.init()

'''Menu loop'''
def menuloop(frame:pygame,player:object,enemies:array,background:object,bullets:array,run:bool):
    run = run

    #Loop
    while run == True:

        '''Keyboard reader'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
                    Status  =False,''
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
                    Status =True,'spl'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    run = False
                    Status =True,'mpml'
        
        '''Deactivate bullets, enemies and player'''
        for elements in enemies:
            elements.show = False
        for elements in bullets:
            elements.show = False
        player.show = False

        '''Visual function'''
        #Background
        background.draw(frame)
        
        #Player
        player.draw(frame)

        #Letters
        font=pygame.font.SysFont('comic sans',80)
        text= font.render("Welcome to the game",True,(255,255,255))
        frame.blit(text,(50,50))

        #Update frame
        pygame.display.update()
    return Status

'''Pause loop'''
def pauseloop (frame:pygame,player:object,enemies:array,background:object,bullets:array,run:bool,pause:object,dt:object):
    run = run

    #Loop
    while run == True:
        '''Keyboard reader'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
                    return 'ml'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    dt.prev = time_elements.time.time()
                    run = False
                    return None

        '''Visual function'''
        #Background
        background.draw(frame)

        #Bullet
        for elements in bullets:
            elements.draw(frame)
        
        #Enemies
        for elements in enemies:
            elements.draw(frame)
        
        #Player
        player.draw(frame)

        #Pause
        pause.draw(frame)

        #Letters
        font=pygame.font.SysFont('comic sans',80)
        text= font.render("Pause",True,(255,255,255))
        frame.blit(text,(520,50))

        #Update frame
        pygame.display.update()

'''General loop for the single player game'''
def mainloop (frame:pygame,player:object,dt:object,enemies:array,background:object,bullets:array,run:bool,pause:object):

    '''Set basic elements for the loop'''
    #Variables
    game = run
    Status = None
    
    #Deltatime
    dt.prev=0

    #Start position of elements
    for elements in enemies:
        elements.setposition(50,50)
        elements.show=True
    player.setposition(580,300)
    player.show = True
    player.life=100
    
    #Loop
    while game == True:

        '''Deltatime'''
        deltatime=dt.calc_dt()

        '''Keyboard reader'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dt.run = False
                game = False
                return False,''
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.cont_move('a',True)
                elif event.key == pygame.K_d:
                    player.cont_move('d',True)
                elif event.key == pygame.K_SPACE:
                    pass
                    #objects[2].shoot()
                elif event.key == pygame.K_ESCAPE:
                    pausebreak = pauseloop(frame,player,enemies,background,bullets,run,pause,dt)
                    if pausebreak == 'quit':
                        dt.run = False
                        game = False
                        return False,''
                    elif pausebreak == 'ml':
                        game = False
                        Status = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.cont_move('a',False)
                elif event.key == pygame.K_d:
                    player.cont_move('d',False)

        '''Objects operations'''
        #Bullets
        for elements in bullets:
            elements.hit(player,deltatime)

        
        #Enemies
        for elements in enemies:
            elements.AI(deltatime,player,bullets)
            if elements.yposition >= 400:
                game = False
                Status = False

        #Player
        if player.life == 0:
            game = False
            Status = False
        player.keymove(deltatime)

        '''Visual function for all of the game elements'''
        #Background
        background.draw(frame)

        #Bullet
        for elements in bullets:
            elements.draw(frame)
        
        #Enemies
        for elements in enemies:
            elements.draw(frame)
        
        #Player
        player.draw(frame)

        #Extra operations
        pygame.display.update()

    #Verificate the break of the loop
    if Status == None:
        dt.run = False
        return False,''
    elif Status == False:
        return True,'ml'
    elif Status == True:
        return True,'ml'

'''Loop for charge'''
def loadingloop (frame:pygame,load:array,background:object,pause:object):

    '''Set the charge process and variable for end loading loop'''
    ready = False
    #Thread  for charge required elements
    t1 =threading.Thread(target=exctrafunctions.mpstart(load))
    elements = t1.start()

    #Loop
    while ready == False:
        #Verif if thread end
        if elements != None:
            ready = True
            return True,'mpl',elements
        
        '''keyboard reader'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ready = True
                return False,'',elements

        '''Visual elements'''
        #Background
        background.draw(frame)

        #Pause
        pause.draw(frame)

        #Letters
        font=pygame.font.SysFont('comic sans',80)
        text= font.render("Loading",True,(255,255,255))
        frame.blit(text,(500,50))

        #Update frame
        pygame.display.update()
    