from swearcheck import * 
from swearReplaceMain import *
import imdb

def getMenuOption(debug = False):
    if debug: print("Get menu option")
    
    goodInput = False
    
    while not goodInput:
        option = input(">")
        option = option.lower()
        
        if (option == "q"
            or option == "quit"
            or option == "exit"):
                option = "q"
                goodInput = True
        elif (option == "1"
            or option == "one"
            or option == "story1"
            or option == "story 1"):
                option = "1"
                goodInput = True
        elif (option == "2"
            or option == "two"
            or option == "story2"
            or option == "story 2"):
                option = "2"
                goodInput = True
        elif (option == "3"
            or option == "three"
            or option == "story3"
            or option == "story 3"):
                option = "3"
                goodInput = True
        elif option == "5":
                goodInput = True
                option = "4"
        else:
            print("Invalid option")
    return option





def getWord(prompt, debug = False):
    if debug: print("Get word option")
    
    goodInput = False
    
    while not goodInput:
        
        word = input(prompt)
        goodInput=True
        
        if word =="":
            print("\nUm, there is no text here...\nPlease enter actual text\n")
            goodInput=False

        elif isAlsoSwear(word, debug):
            goodInput = False
            print("Foul languge detected!")
            print("Bad user, enter a different word, NOT A SWEAR!\n")
    return word
    
    
def getWordAAn(prompt, debug = False):
    if debug: print("Get word option a an")
    
    word = getWord(prompt, debug)
    
    vouals=['a','e','i','o','u']
    
    if word[0] in vouals:
        word = "an "+word
    else:
        word = "a "+word
        
    return word
    
    

def getSwear(prompt, debug = False):
    if debug: print("getSwear function")
    goodWord = False
    while goodWord == False:
        swear = input(prompt)
        if isAlsoSwear(swear, False, True):
            goodWord = True
            replaceSwear(swear, debug)
        else: 
            goodWord = False
            wantSwear = input("do you just not want to swear? (it's ok if you don't, input 'yes') > ")
            if wantSwear == "yes": goodWord = True
    return replaceSwear(swear, debug)
#robert's little testy bits for getSwear function
#test=getSwear("swear, please > ", False)
#print(test)

#ryab reynolds movie getter
#Imported imdb at the top. 
#ia = imdb.Cinemagoer()
#
#
#rr = ia.get_person('0005351')
#roles = rr['filmography']['actor']
#titles = []
#for role in roles:
#	titles += [role["title"].lower()]
#this is copied and works.
#grab ryan reynolds on imdb, find movies where he is actor. 
#make list
#get input
#if input lower is in the list, good input
#else, try again
#use that as madlib word

def getRyanReynoldsMovie(prompt = "000", debug = False):
    if debug: print("getRyanReynoldsMovie function")
    ia = imdb.Cinemagoer()


    rr = ia.get_person('0005351')
    roles = rr['filmography']['actor']
    titles = []
    for role in roles:
        titles += [role["title"].lower()]
    goodInput = False
    while goodInput == False:
        rrMovieInput = input(prompt)
        if rrMovieInput.lower() in titles:
            goodInput = True
            if debug: print("goodInput set to true"), print(rrMovieInput)
            return rrMovieInput
        else: goodInput = False, print("Not a Ryan Reynolds movie, try again.") if debug: print("goodInput set to false") 

testOutput = getRyanReynoldsMovie("test it broski > ", True)
print(testOutput)
