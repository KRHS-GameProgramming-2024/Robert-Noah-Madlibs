from Getters import *



def Story1(debug=False):
    if debug: print("Story 1")
    
    person=getWord("Enter the name of your best friend ", debug)
    place=getWord("Enter the name of a place ", debug)
    danger=getWord("Enter the name of something dangorus ", debug)
    largeObject=getWord("Enter the name of something big ", debug)
    bad=getWord("Enter a horrible way to die: ", debug)
    people=getWord("Enter a horrible group of people: ", debug)

    
    
    
    out = "\n"
    out += person +" was at/in the "
    out += place+" and was killed by a(n) "
    out += danger +'. \n'
    out += person+ " was also crushed by a(n) "
    out += largeObject+".\n"+'That morning, '
    out += person+" barely escaped being "
    out += bad+" to death by "
    out += people+"."
    
    
    return out