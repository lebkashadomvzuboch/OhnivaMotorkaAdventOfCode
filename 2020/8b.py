kod = []

class Pokazeny(Exception):
    pass

class Opraveny(Exception):
    pass

with open("adventofcode/OhnivaMotorkaAdventOfCode/input.txt", "r") as subor:
    for riadok in subor.readlines():
        kod.append(riadok.strip())

def spracuj_input(pointer, accumulator, bolo, kod_):
    if pointer == len(kod_):
        raise Opraveny

    if bolo[pointer]:
        raise Pokazeny
    
    bolo[pointer] = True
    prikaz, cislo = kod_[pointer].split()
    
    if prikaz == "acc":
        accumulator += int(cislo)
    elif prikaz == "jmp":
        pointer += int(cislo) - 1

    return pointer+1, accumulator, bolo

def otestuj(kod_):
    bolo = [False for i in range(len(kod_))]
    accumulator = 0
    pointer = 0
    while True:
        try:
            pointer, accumulator, bolo = spracuj_input(pointer, accumulator, bolo, kod_)
        
        except Pokazeny:
            return False

        except Opraveny:
            return accumulator


for index_riadku in range(len(kod)):
    if not kod[index_riadku].startswith("acc"):
        oprava = kod[index_riadku].replace("nop", "jmp") if "nop" in kod[index_riadku] else kod[index_riadku].replace("jmp", "nop")
        novy_kod_na_overenie = kod[:index_riadku] + [oprava] + kod[index_riadku+1:]
        
        vysledok = otestuj(novy_kod_na_overenie)
        if vysledok:
            print(vysledok)
            break

# vysledok je 767
