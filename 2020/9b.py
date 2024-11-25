riadky = []
cislo = 466456641

with open("adventofcode/OhnivaMotorkaAdventOfCode/input.txt", "r") as subor:
    for riadok in subor:
        riadky.append(int(riadok.strip()))

preable_dlzka = 25

for i in range(len(riadky)):
    porovnavacie_cislo = [riadky[i]]
    pc = 0
    while sum(porovnavacie_cislo) < cislo:
        pc += 1
        porovnavacie_cislo.append(riadky[i+pc])
    else:
        if sum(porovnavacie_cislo) == cislo:
            print(max(porovnavacie_cislo) + min(porovnavacie_cislo))
            break

# vysledok je 55732936