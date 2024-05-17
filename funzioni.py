import random


def tartaruga(t: int) -> int:
    x: int = random.randint(1,10)
    if x <= 5:
        t += 3
    elif x >= 6 and x <= 7:
        t -= 6
    else:
        t += 1
    if t <= 0:
        t = 1
    return t

def lepre(h: int) -> int:
    x: int = random.randint(1,10)
    if x >= 1 and x <= 2:
        h += 0
    elif x >= 3 and x <= 4:
        h += 9
    elif x == 5:
        h -= 12
    elif x >= 6 and x <= 8:
        h += 1
    else:
        h -= 2
    if h <= 0:
        h = 1
    return h

def tartaruga_meteo(t: int, meteo: str) -> int:
    x: int = random.randint(1,10)
    if meteo == "PIOGGIA":
        t -= 2
    if x <= 5:
        t += 3
    elif x >= 6 and x <= 7:
        t -= 6
    else:
        t += 1
    if t <= 0:
        t = 1
    return t

def lepre_meteo(h: int, meteo: str) -> int:
    x: int = random.randint(1,10)
    if meteo == "PIOGGIA":
        h -= 2
    if x >= 1 and x <= 2:
        h += 0
        if meteo == "PIOGGIA":
            h += 2
    elif x >= 3 and x <= 4:
        h += 9
    elif x == 5:
        h -= 12
    elif x >= 6 and x <= 8:
        h += 1
    else:
        h -= 2
    if h <= 0:
        h = 1
    return h

def check(t: int, h: int) -> bool:
    if t >= 70 and h >= 70:
        print("IT'S A TIE.")
        return True
    elif h >= 70 and t < 70:
        print("HARE WINS || YUCH!!!")
        return True
    elif t >= 70 and h <= 70:
        print("TORTOISE WINS! || VAY!!!")
        return True
    else: 
        return False

def posizioni(percorso: list, t: int, h: int) -> None:
    for x in range(len(percorso)):
        if t == h and x+1 == t:
            print("OUCH!!!",end="")
        elif (x+1) == t: #and (x+1) != h:
            print("T",end="")
        elif (x+1) == h: #and (x+1) != t:
            print("H",end="")
        else:
            print("-",end="") #percorso[x]