hasPygame=False
try:
    from pygame import mixer
    hasPygame=True
except:
    input("Missing Pygame liberarys :(  (Type yes to install)\n>")

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

    mixer.music.load("song.mp3")
    mixer.music.play()
    
    ################################
    #IMPORTANT!!!!!
    
    #Music I Use: Bensound.com/free-music-for-videos
    #License code: QYHFL1RRSO9JBEBZ
    
    
def easterEggPoker():
    theDeck = [
    
