kod = []

with open("adventofcode/OhnivaMotorkaAdventOfCode/input.txt", "r") as subor:
    for riadok in subor.readlines():
        kod.append(riadok.strip())

bolo = [False for i in range(len(kod))]
accumulator = 0
pointer = 0


def spracuj_input(pointer, accumulator, bolo):
    if bolo[pointer]:
        print(accumulator)
        raise ValueError
    bolo[pointer] = True
    prikaz, cislo = kod[pointer].split()
    
    if prikaz == "acc":
        accumulator += int(cislo)
    elif prikaz == "jmp":
        pointer += int(cislo) - 1

    return pointer+1, accumulator, bolo

while True:
    try:
        pointer, accumulator, bolo = spracuj_input(pointer, accumulator, bolo)
    
    except ValueError:
        break

# vysledok je 1563

