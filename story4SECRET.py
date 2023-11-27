hasPygame=False
try:
    from pygame import mixer
    hasPygame=True
except:
    print("Missing Pygame liberaries :( ")

from Getters import *
import os


mixer.init()
os.system('cls')


def Story4SECRET(debug=False):
    if debug: print("Drop D, 92 BPM")
    
    out =  "I'm not dating Liz"
    out += "\n stop"
    
    return out
#print(Story4SECRET())

def audioPlay():
    if not hasPygame:
        print('This function is unavalile, please install pygame in order to continue')
    else:
        mixer.music.load("song.mp3")
        mixer.music.play()
    
    ################################
    #IMPORTANT!!!!!
    
    #Music I Use: Bensound.com/free-music-for-videos
    #License code: QYHFL1RRSO9JBEBZ
    
    
#def easterEggPoker():
#    theDeck = [
#    
#
def easterChatBot(debug = False):
    rr = ia.get_person('0005351')
    roles = rr['filmography']['actor']
    titles = []
    for role in roles:
        titles += [role["title"].lower()]

    print("hello, I am the crap-bot")

    favoriteNumber = int(input("What is your favorite number? "))
    print("my favorite number is 6")
    if 6+1 == favoriteNumber or 6-1 == favoriteNumber:
        print("your favorite number is not bad")
    elif favoriteNumber == 6:
        print("good favorite number")
    name = input("what is your name ")
    if name[-1]=="a":
        print("what kind of a name is ", name)
        print("only crazy people have names that end with the 'uh' sound")
    elif name.lower() == "ryan reynolds":
        isRR = input("is it really you? ")
        if isRR == yes:
            print("how great to meet you")
        else:
            print("I can't beleive you would lie like that")	
    else:
        print("that's a fire name")
        print("I'm glad your name doesn't end in the 'uh'  sound")
        print("never change your name to Angelica or Karen or Kenny")
    age = int(input("how old are you? "))
    if age < 18:
        print("you're a little too young for this chat bot. ")
        quit()
    else:
        print("you are old enough for this chat bot")
    favoriteMovie = input("what's your favorite movie? ")
    if favoriteMovie.lower() in titles:
        print("That movie is awesome. I like all of the movies with Ryan Reynolds.")
    else:
        print("you disqusting, uncivilized, distasteful wretch.")


def chatScreenStart(debug = False):
    if debug: print("showchatScreen")
    
    out = "------------------------------------\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="  hello                             |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="************************************"
    
def chatScreen(debug = False):
    if debug: print("showchatScreen")
    
    out = "------------------------------------\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="                                    |\n"
    out +="************************************"
