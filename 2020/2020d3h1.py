vysledok = 0
les = []
doprava, dole = 3, 1


with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        les.append(riadok.strip())

vyska_lesa, sirka_lesa = len(les), len(les[0])

aktualna_sirka = 0

for riadok in range(dole, vyska_lesa):
    aktualna_sirka += doprava

    aktualna_sirka = aktualna_sirka % sirka_lesa

    if les[riadok][aktualna_sirka] == "#":
        vysledok += 1

print(vysledok)

# vysledok je 268
