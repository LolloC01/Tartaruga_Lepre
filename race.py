import random
import funzioni as f

percorso: list = ["_"] * 70
energia_t = energia_h = 100
t = h = c = m = 0

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


def mov_energia_t(t: int, meteo: str) -> int:
    x: int = random.randint(1,10)
    global energia_t
    if x <= 5 and f.check_energy(energia_t, 5):
        energia_t -= 5
        t += 3
    elif x >= 6 and x <= 7 and f.check_energy(energia_t, 10):
        energia_t -= 10
        t -= 6
    elif x >= 8 and x <= 10 and f.check_energy(energia_t, 3):
        energia_t -= 3
        t += 1
    else:
        print("Tartaruga recupera energia")
        if energia_t <= 90:
            energia_t += 10
        elif energia_t > 90:
            energia_t = 100
        t += 0
    if t <= 0:
        t = 1
    t = f.check_meteo(meteo, t, 1)
    return t


def mov_energia_h(h: int, meteo: str) -> int:
    x: int = random.randint(1,10)
    global energia_h
    if x >= 1 and x <= 2:
        print("Lepre ferma recupera energia")
        if energia_h <= 90:
            energia_h += 10
        elif energia_h > 90:
            energia_h = 100
        h += 0
        return h
    elif x >= 3 and x <= 4 and f.check_energy(energia_h, 15):
        energia_h -= 15
        h += 9
    elif x == 5 and f.check_energy(energia_h, 20):
        energia_h -= 20
        h -= 12
    elif x >= 6 and x <= 8 and f.check_energy(energia_h, 5):
        energia_h -= 5
        h += 1
    elif x >= 9 and x <= 10 and f.check_energy(energia_h, 8):
        energia_h -= 8
        h -= 2
    else:
        print("Lepre recupera energia")
        if energia_h <= 90:
            energia_h += 10
        elif energia_h > 90:
            energia_h = 100
        h += 0
    if h <= 0:
        h = 1
    h = f.check_meteo(meteo, h, 2)
    return h


malus = {15 : -3,
         30 : -5,
         45 : -7}

bonus = {10 : 5,
         25 : 3,
         50 : 10}

def check_ostacoli(animal: int) -> int:
    if animal in bonus:
        print("BONUS")
        animal += bonus[animal]
        return animal
    elif animal in malus:
        print("MALUS")
        animal += malus[animal]
        return animal
    return animal

time: int = 0
print("BANG !!!!! AND THEY'RE OFF !!!!!")
while True:
    current_meteo = meteo()
    #t = f.tartaruga_meteo(t, current_meteo)
    #h = f.lepre_meteo(h, current_meteo)
    t = mov_energia_t(t, current_meteo)
    h = mov_energia_h(h, current_meteo)
    print("tartaruga")
    t = check_ostacoli(t)
    print("lepre")
    h = check_ostacoli(h)
    f.posizioni(percorso,t,h)
    
    print(c)
    if f.check(t,h):
        break
    c += 1

