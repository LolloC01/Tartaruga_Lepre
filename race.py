import random
import funzioni as f

percorso: list = ["_"] * 70
energia_t = energia_h = 100
t = h = c = m = 0

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

def meteo() -> str:
    global m
    if m < 10:
        m += 1
        return "PIOGGIA"
    elif m >= 10 and m < 19:
        m += 1
        return "SOLE"
    elif m == 19:
        m = 0
        return "SOLE"
    return 

time: int = 0
print("BANG !!!!! AND THEY'RE OFF !!!!!")
while True:
    current_meteo = meteo()
    t = f.tartaruga_meteo(t, current_meteo)
    h = f.lepre_meteo(h, current_meteo)
    f.posizioni(percorso,t,h)
    print(c)
    if f.check(t,h):
        break
    c += 1

