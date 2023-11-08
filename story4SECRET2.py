hasPygame=False
try:
    from pygame import mixer
    hasPygame=True
except:
    print("Missing liberaries(Pygame)")
    print("Please download liberarys to continue")
    print('(in console type "pip install pygame")')

from Getters import *
import os

mixer.init()
os.system('cls')


def Story4SECRET(debug=False):
    if debug: print("Drop D, 92 BPM")
    
    out =  "I'm not dating Liz"
    out += "\n stop"
    
    return out






def audioPlay():
    if not hasPygame:
        print("This Function is Unavalible, Please install PYGAME")
    else:
        mixer.music.load("song.mp3")
        mixer.music.play()
    
    ################################
    #IMPORTANT!!!!!
    
    #Music I Use: Bensound.com/free-music-for-videos
    #License code: QYHFL1RRSO9JBEBZ
    
    
