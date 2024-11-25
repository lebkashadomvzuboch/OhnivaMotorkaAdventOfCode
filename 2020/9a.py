riadky = []

with open("adventofcode/OhnivaMotorkaAdventOfCode/input.txt", "r") as subor:
    for riadok in subor:
        riadky.append(int(riadok.strip()))

preable_dlzka = 25

for i in range(preable_dlzka, len(riadky)):
    cislo = riadky[i]
    if cislo not in {a+b for a in riadky[i-preable_dlzka:i] for b in riadky[i-preable_dlzka+1:i]}:
        print(cislo)

# vysledok je 466456641