from exctrafunctions import *
from loops import mainloop

#Excecute main loop
if __name__ == "__main__":
    elements = start()
    mainloop(elements['frame'],elements['player'],elements['dt'],elements['objects'])