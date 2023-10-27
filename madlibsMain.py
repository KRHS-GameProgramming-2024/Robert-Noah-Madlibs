from Screens import *
from Getters import *
from Story1 import *
from Story2 import *
from Story3 import *

def Madlibs(debug = False):
    if debug: print("Welcome to madlibs debuging")
    
    
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
        elif option == "2":
            print(Story2(debug))
        elif option == "3":
            print(Story3(debug))
            
        input("Press enter to continue")

        

Madlibs()
