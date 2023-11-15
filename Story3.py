from Getters import *
import os
clear = lambda: os.system('cls')

#for friend house
#Robert
def Story3(debug=False):
    if debug: print("Story 3")
    
    RrMovie = getRyanReynoldsMovie("Name a Ryan Reynolds movie. > ", debug)
    clear()
    List = friendsHouseFunction(debug)
    clear()
    activity = getWord("Name something you would do at a friend's house > ")
    clear()
    howeverLong = getWord("How long were they there? > ", debug)
    clear()
    food = getWord("What did they eat? > ", debug)
    clear()
    otherFood = getWord("What other thing did they eat? > ", debug)
    clear()
    friend1=List[0]
    friend2=List[1]
    friendsHouse = List[2]
    
    
    
    out = ""
    out +="One day, " + friend1 + " and " + friend2 + " were at " + friendsHouse + "." +"\n"
    out +="They ate " + food + " and " + otherFood + ".\n"
    out +="After eating, they wanted to " + activity + " and watch " + RrMovie + ".\n"
    out +="They were at " + friendsHouse + " for " + howeverLong + "."
    return out
#goodHouse = False
#debug = False
#check to see if the input is one of the friends names. If not, try again. If, add an "'s house" house to the end. If last letter is a space, exclude.
#friend1 = getWord("Name one friend > ", debug)
#friend2 = getWord("Name another friend > ", debug)
#while not goodHouse:
#    friendsHouse = input("Who's house do they go to?")
#    if friendsHouse in friend1:
#        if friendsHouse[-1] == " ":
#            friendsHouse = friendsHouse[:-1]
#        goodHouse = True
#        friendsHouse += "'s house"
#    elif friendsHouse in friend2:
#        if friendsHouse[-1] == " ":
#            friendsHouse = friendsHouse[:-1]
#        goodHouse = True
#        friendsHouse += "'s house"
#    else: goodHouse = False
#print(friendsHouse)
#print(Story3())
