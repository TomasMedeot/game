import threading
import pygame

'''General loop for the game'''
def mainloop (frame,player,dt,objects):
    game = True
    
    #deltatime subproces
    dtime=threading.Thread(target=dt.fp)
    dtime.start()
    
    #loop
    while game == True:
        '''Keyboard reader'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dt.run = False
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.cont_move('a',True)
                elif event.key == pygame.K_d:
                    player.cont_move('d',True)
                elif event.key == pygame.K_SPACE:
                    pass
                    #objects[2].shoot()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.cont_move('a',False)
                elif event.key == pygame.K_d:
                    player.cont_move('d',False)

        '''objects operations'''
        #General objects
        for elements in objects:
            objects[2].AI(player,objects[1],dt.miliseconds)

        #Player operations
        player.keymove(dt.miliseconds)

        '''Visual function for all of the game elements'''
        #General render
        for elements in objects:
            elements.draw(frame)
        #Player render
        player.draw(frame)

        #Extra operations
        dt.frame = dt.frame + 1
        pygame.display.update()