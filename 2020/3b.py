les = []
moznosti = {(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)}

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        les.append(riadok.strip())

vyska_lesa, sirka_lesa = len(les), len(les[0])


def smykaj_sa(doprava, dole):
    aktualna_sirka = 0
    vysledok = 0
    for riadok in range(dole, vyska_lesa, dole):
        aktualna_sirka += doprava
        aktualna_sirka = aktualna_sirka % sirka_lesa

        if les[riadok][aktualna_sirka] == "#":
            vysledok += 1

    return vysledok


vysledok = 1
for v in [smykaj_sa(i[0], i[1]) for i in moznosti]:
    vysledok *= v
    print(v)

print(vysledok)

# vysledok je 3093068400
