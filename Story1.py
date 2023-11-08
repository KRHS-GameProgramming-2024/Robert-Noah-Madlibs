from Getters import *
import os
clear = lambda: os.system('cls')

#noah
def Story1(debug=False):
    if debug: print("Story 1")
    
    person=getWord("Enter the name of your best friend ", debug)
    clear()
    place=getWord("Enter the name of a place ", debug)
    clear()
    danger=getWordAAn("Enter the name of something dangorus ", debug)
    clear()
    largeObject=getWordAAn("Enter the name of something big ", debug)
    clear()
    bad=getWord("Enter a horrible way to die: ", debug)
    clear()
    people=getWord("Enter a horrible group of people: ", debug)
    clear()
    
    
    
    out = ""
    out += person +" was at/in the "
    out += place+" and was killed by "
    out += danger +'. \n'
    out += person+ " was also crushed by "
    out += largeObject+".\n"+'That morning, '
    out += person+" barely escaped being "
    out += bad+" to death by "
    out += people+"."
    
    
    return out
