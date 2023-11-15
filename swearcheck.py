

def isSwear(word, debug=False, wordDetect=False):
    if debug: print("swear checker")
    if word.lower() in swearList:
        return True
    else:
        return False

def allPos(word, debug = False, wordDetect=False):
    if debug: print("allpos swear checker")

    

    if len(word)<3:
        return False
    #I have incorberated this if len<3 because if the word they enter is less than 3 characters long it cant be a swear in swear list because all swears in swearlist are 3 or more characters
    
    worb="n"+word
    
    for x in worb:
        worb = worb[1:len(worb)]
        t=""
        for i in worb:
            t+=i
            if debug: print(t)
            if isSwear(t, debug):
                #gotta disable this for a special getter
                #I think if !variable should work, but we would 
                #need to import getters, weird imports might cause
                #problems. Anyhow, try:
                # from getters import [what we need to import]
                #if !specialSwearGetter: print("\nWord detected! string
                #we also need to add that pos. argu. to whatever functions call that string
                if not wordDetect:
                    print("\nWord detected! Word found is "+t+"!") 
                return True
    return False




def isAlsoSwear(word, debug = False, wordDetect=False):
    if debug: print("isAlsoSwear swear checker")
    word=word.lower()
    
    if allPos(word,debug, wordDetect):
        return True
    
    test1=""
    
    for x in word:
        if x in aList:
            test1+=x
    
    if debug:
        print(test1)
    
    if allPos(test1):
        return True
    
    return allPos(word)

    wordTest=""
    
    for i in word:
        if i == "@" or i == "4":
            wordTest+="a"
        elif i=="8":
            wordTest+="b"
        elif i == "(" or i == "<":
            wordTest += "c"
        elif i == "3":
            wordTest += "e"
        elif i == "!" or i == "1" or i == "|" or i == "l":
            wordTest +="i"
        elif i == "0":
            wordTest +="o"
        elif i =="$":
            wordTest+="$"
        else:
            wordTest+=i
            
    if allpos(wordTest,debug):
        return True

    
    
'''
a=@
a=4

b=8
b=3

c=(
c=<

e=3

i=!
i=1
i=|
i=l


o=0

s=$


'''








aList = ["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']





















swearList = ["ass", #A
                "arse",
                "alabamaporch-monkey",
                "alligatorbabe",
                "african",
                "americancoptargetpractice",
                #B
                "bitch",
                "black",
                "beaner",
                "bibi",
                "buddha-head",
                "basketballperson",
                "basketballpeople",
                "brown",
                #C
                "cunt",
                "cock",
                "cracker",
                "duckie",
                "coolieheeb",
                "christ-killer",
                "cameljockey",
                "towelhead",
                "coco-puff",
                "cropmakaka",
                #D
                "dick",
                "damn",
                #E
                "enginejap",
                #F
                "fag",
                "fagg",
                "faggot",
                "fuck",
                "friedchickenpeople",
                #G
                "geriatric",
                "god",
                "golliwog",
                "gringo",
                "gypsy",
                "gay",
                #H
                "high-meat",
                "happyhaji",
                "hairyback",
                "harbor-bomber",
                #I
                "indian",
                #J
                "junglebunny",
                "jew",
                "juju",
                #K
                "kungofu",
                "kkk",
                #L
                "lanieorio",
                #M
                "moghwai",
                "muzzie",
                "mexican",
                "mexajew",
                "mexa-jew",
                #N
                "nigger",
                "nigga",
                "ni66er",
                "ni66a",
                "nigg3r",
                "ni663r",
                "niglet",
                "nig-nog",
                "negro",
                "nazi",
                "noah zorilla"
                #O
                #P
                "pickaninny",
                "penis",
                "potatoeater",
                "poo",
                "panda",
                #Q
                "queer",
                #R
                "redneck",
                "redskin",
                "rice-patty",
                "retarded",
                "bibi",
                "buddha-head",
                #S
                "slant-eye",
                "slave",
                "skibiditoilet",
                "scamcaller",
                #T
                "taco-whopper",
                #U
                "uncletom",
                "urmom",
                'yourmom',
                "yurmom",
                #V
                "vagina",
                #W
                "wetback",
                "fatty",
                "wonderbread",
                "watermelonlover",
                "whitedevil",
                "white",
                #X
                #Y
                "yellow-red",
                #Z
                "zebra-twinkie",
                ]

