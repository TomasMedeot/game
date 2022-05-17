import threading
import pygame

'''General loop for the game'''
def mainloop (frame,player,dt,objects):
    game = True
    
    #deltatime subproces
    dtime=threading.Thread(target=dt.calc_dt)
    dtime.start()
    
    #loop
    while game == True:
        #print(dt.deltatime)

        '''Keyboard reader'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.keymove(5,'a')
                elif event.key == pygame.K_d:
                    player.keymove(5,'d')
                '''elif event.key == pygame.K_SPACE:
                    objects[2].shoot()'''

        '''objects operations'''
        for elements in objects:
            objects[2].AI(player,objects[1],1)

        '''Visual function for all of the game elements'''
        for elements in objects:
            elements.draw(frame)
            player.draw(frame)
        pygame.display.update()