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

def posizioni(percorso: list, t: int, h: int) -> None:
    for x in range(len(percorso)):
        if t == h and x+1 == t:
            print("OUCH!!!",end=" ")
        elif (x+1) == t and (x+1) != h:
            print("T",end=" ")
        elif (x+1) != t and (x+1) == h:
            print("H",end=" ")
        else:
            print("-",end=" ") #percorso[x]

def posizione(percorso: list, t: int, h: int) -> None:
    for x in range(len(percorso)):
        if t == h and x+1 == t:
            percorso[x] = "OUCH!!!"
        elif (x+1) == t and (x+1) != h:
            percorso[x] = "T"
        elif (x+1) != t and (x+1) == h:
            percorso[x] = "H"
        else:
            percorso[x] = "_"
    print(percorso)

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

def meteo(m, t, h) -> int:
    if m < 10:
        print("PIOGGIA")
        t -= 1
        h -= 2
        m += 1
    elif m >= 10 and m < 19:
        print("SOLE")
        m += 1
    elif m == 19:
        print("SOLE")
        m = 0
    return m, t, h


def mov_energia_t(energia_t: int, t) -> int:
    x: int = random.randint(1,10)
    if x <= 5 and energia_t >= 5:
        energia_t -= 5
        t += 3
    elif x >= 6 and x <= 7 and energia_t >= 10:
        energia_t -= 10
        t -= 6
    elif x >= 8 and x <= 10 and energia_t >= 3:
        energia_t -= 3
        t += 1
    else:
        print("Tartaruga recupera energia")
        if energia_t <= 90:
            energia_t += 10
        elif energia_t > 90 and energia_t < 100:
            energia_t = 100
        t += 0
    if t <= 0:
        t = 1
    return energia_t, t

def mov_energia_h(energia_h: int, h: int) -> int:
    x: int = random.randint(1,10)
    if x >= 1 and x <= 2:
        print("Lepre ferma recupera energia")
        if energia_h <= 90:
            energia_h += 10
        elif energia_h > 90 and energia_h < 100:
            energia_h = 100
        h += 0
    elif x >= 3 and x <= 4 and energia_h >= 15:
        energia_h -= 15
        h += 9
    elif x == 5 and energia_h < 100:
        energia_h -= 20
        h -= 12
    elif x >= 6 and x <= 8 and energia_h < 100:
        energia_h -= 5
        h += 1
    elif x >= 9 and x <= 10 and energia_h < 100:
        energia_h -= 8
        h -= 2
    else:
        print("Lepre recupera energia")
        if energia_h <= 90:
            energia_h += 10
        elif energia_h > 90 and energia_h < 100:
            energia_h = 100
        h += 0
    if h <= 0:
        h = 1
    return energia_h, h


percorso: list = ["_"] * 70
energia_t = energia_h = 100
t = h = c = m = 0
print("BANG !!!!! AND THEY'RE OFF !!!!!")
while True:
    energia_t, t = mov_energia_t(energia_t, t)
    energia_h, h = mov_energia_h(energia_h, h)
    m, t, h = meteo(m, t, h)
    posizioni(percorso,t,h)
    print(c)
    if check(t,h):
        break
    c += 1

