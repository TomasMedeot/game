from exctrafunctions import *
from loops import loadingloop, mainloop, menuloop

#Excecute main loop
if __name__ == "__main__":
    elements = start()
    run = True
    status = 'ml'
    while run == True:
        if status == 'ml':#Menu loop
            run,status=menuloop(elements['frame'],elements['player'],elements['enemies'],elements['background'],elements['bullets'],run)
        elif status == 'mpml':#Multi player Menu loop
            status = 'lmpl'
        elif status == 'lmpl':#Loading multi player loop
            run,status,mpelements=loadingloop(elements['frame'],[],elements['background'],elements['pause'])
        elif status == 'mpl':#Multi player loop
            pass
        elif status == 'spl':#Simple player loop
            run,status=mainloop(elements['frame'],elements['player'],elements['dt'],elements['enemies'],elements['background'],elements['bullets'],run,elements['pause'])