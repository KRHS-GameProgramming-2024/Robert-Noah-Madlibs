from Getters import *
import os
clear = lambda: os.system('cls')
#Robert
def Story2(debug=False):
    if debug: print("this is debug mode of story 2\n")
    noun = getWord("Enter a thing: ", debug)
    clear()
    verb = getWord("Enter a action: ", debug)
    clear()
    person = getWord("Enter a name: ", debug)
    clear()
    place = getWord("Enter a place: ", debug)
    clear()
    event = getWord("Enter a event: ", debug)
    clear()
    sillyThing = getWord("Enter a silly thing: ", debug)
    clear()
    monster = getWord("Enter a monster: ", debug)
    clear()
    color = getWord("Enter a color: ", debug)
    clear()
    cuss =   getSwear("swear please > ", debug)
    clear()
    
    letters = "One fine evening, " + person
    letters += " had a craving to " + verb + "\n" 
    letters += "until the sun began to rise. " + person+"\n"
    letters += "would do it at the " + event
    letters += " at " + place + ",\n"
    letters += "and he would bring a " + sillyThing +". "
    letters += "It was " + color + ".\n"
    letters += "When " + person + " got to the " + event + " at " + place+",\n"
    letters += "the " + monster + " at the door called him a " + cuss + ". \n"
    letters += person + "went home disappointed.\n"
    return letters
