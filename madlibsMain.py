#test
from Screens import *
from Getters import *
from Story1 import *
from Story2 import *
from Story3 import *
import os
clear = lambda: os.system('cls')



def Madlibs(debug = False):
    if debug: print("Welcome to madlibs debuging")
    clear()
    
    print(showSplashScreen(debug))
    input("Press enter to continue")
    clear()
    
    done=False
    while not done:
        print(showMenuScreen(debug))
        option=getMenuOption(debug)
        clear()
        if option == "q":
            exit()
        elif option == "1":
            print(Story1(debug))
        elif option == "2":
            print(Story2(debug))
        elif option == "3":
            print(Story3(debug))
            
        input("Press enter to continue")
        clear()

        

Madlibs()
