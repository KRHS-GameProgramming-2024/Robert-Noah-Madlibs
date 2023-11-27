from Screens import *
from Getters import *
from Story1 import *
from Story2 import *
from Story3 import *
from story4SECRET import *
from random import *
import time
#pip install IMDbPY


import os
clear = lambda: os.system('cls')

def Madlibs(debug = False):
    doGame = True
    if debug: print("Welcome to madlibs debuging")
    time.sleep(3)
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
        elif option == "4":
            print(Story4SECRET(debug))
            audioPlay()
            playPoker = input("would you like to play 1 hand of poker? type 'yes' to play. ")
            clear()
            if playPoker == "yes":
                easterEggPoker(debug)
        elif option == "c":
            print(Credits(debug))
            s=input()
            clear()
            if s == "m":
                print(Musiccredits(debug))
            
            
        input("Press enter to continue")
        clear()

        

Madlibs(False)
