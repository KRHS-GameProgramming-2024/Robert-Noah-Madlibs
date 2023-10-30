from swearcheck import * 


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
    
    
