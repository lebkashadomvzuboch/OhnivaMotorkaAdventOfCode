vysledok = 0

stlpce = [[], [], []]

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        cisla = [int(i.strip()) for i in riadok.strip().split(" ") if i.strip() != ""]
        
        for i in range(3):
            stlpce[i].append(cisla[i])

for stlpec in stlpce:
    for i in range(0, len(stlpec), 3):
        cisla = [stlpec[i], stlpec[i+1], stlpec[i+2]]
        cisla.sort()
        if cisla[0] + cisla[1] > cisla[2]:
            vysledok += 1


print(vysledok)

# vysledok je 1921
