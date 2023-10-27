#robert was here
from Screens import *
from Getters import *
from Story1 import *

def Madlibs(debug = False):
    if debug: print("welcome to madlibs debuging")
    
    
    print(showSplashScreen(debug))
    input("Press enter to continue")
    
    
    done=False
    while not done:
        print(showMenuScreen(debug))
        option=getMenuOption(debug)
        if option == "q":
            exit()
        elif option == "1":
            print(Story1(debug))
            
        input("Press enter to continue")

        

Madlibs()
