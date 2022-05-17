from functions import *
from mainloop import mainloop

#ejecutable 
if __name__ == "__main__":
    elements = start()
    mainloop(elements['frame'],elements['player'],elements['dt'],elements['objects'])