def replaceSwear(swear, debug):
    out = ""
    for index, letter in enumerate(swear):
        if index == 0:
            out += letter
        elif letter == "a":
            out += "@"
        elif letter == "b":
            out += "8"
        elif letter == "c":
            out += "("
        elif letter == "d":
            out += "4"
        elif letter == "e":
            out += "3"
        elif letter == "f":
            out += "4"
        elif letter == "g":
            out += "&"
        elif letter == "h":
            out += "#"
        elif letter == "i":
            out += "!"
        elif letter == "j":
            out += "7"
        elif letter == "k":
            out += "%"
        elif letter == "l":
            out += "1"
        elif letter == "m":
            out += "3"
        elif letter == "n":
            out += ">"
        elif letter == "o":
            out += "0"
        elif letter == "p":
            out += "9"
        elif letter == "q":
            out += "9"
        elif letter == "r":
            out += "&"
        elif letter == "s":
            out += "5"
        elif letter == "t":
            out += "#"
        elif letter == "u":
            out += "("
        elif letter == "v":
            out += "{"
        elif letter == "w":
            out += "}"
        elif letter == "x":
            out += "%"
        elif letter == "y":
            out += "&"
        elif letter == "z":
            out += "Z"
        else:
            out += letter
            if debug: print("if you see this print, go to file swearLetterReplace, you missed something")
    return out

#print(replaceSwear("the quick brown fox jumped over the lazy dog", False))
