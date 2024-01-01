morske_dno = []
smery = ((1, 0), (0, 1), (-1, 0), (0, -1))
basins = []
basins_values = []
uz_bolo = []

with open('input_.txt', "r") as subor:
    for riadok in subor.readlines():
        morske_dno.append([int(i) for i in riadok.strip()])

pocet_riadkov, pocet_stlpcov = len(morske_dno), len(morske_dno[0])

for riadok in range(pocet_riadkov):
    for stlpec, cislo in enumerate(morske_dno[riadok]):
        je_najnizsie = True

        for smer in smery:
            if 0 <= riadok + smer[0] < pocet_riadkov and 0 <= stlpec + smer[1] < pocet_stlpcov:
                if morske_dno[riadok+smer[0]][stlpec+smer[1]] <= cislo:
                    je_najnizsie = False

        if je_najnizsie:
            basins.append((riadok, stlpec))


def flood_fill(riadok, stlpec, total=0):
    if (riadok, stlpec) not in uz_bolo:
        uz_bolo.append((riadok, stlpec))
        if morske_dno[riadok][stlpec] != 9:
            for smer in smery:
                if 0 <= riadok + smer[0] < pocet_riadkov and 0 <= stlpec + smer[1] < pocet_stlpcov:
                    total += flood_fill(riadok+smer[0], stlpec+smer[1])

            return total + 1
        else:
            return 0

    else:
        return 0


for riadok in range(pocet_riadkov):
    for stlpec in range(pocet_stlpcov):
        q = flood_fill(riadok, stlpec)
        if q > 1:
            basins_values.append(q)

basins_values.sort(reverse=True)

print(basins_values[0] * basins_values[1] * basins_values[2])

# vysledok je 916688
# ksp u4 copy
