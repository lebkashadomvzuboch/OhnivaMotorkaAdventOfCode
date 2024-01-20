smery = ((-1, 0), (-1, 1), (-1, -1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

svetielka = []

with open('input.txt', "r") as subor:
    for riadok in subor.readlines():
        svetielka.append([l for l in riadok.strip()])

pocet_riadkov, pocet_stlpcov = 100, 100

rohy = ((0, 0), (0, 99), (99, 0), (99, 99))

for i in range(100):
    zmena = []
    for riadok in range(pocet_riadkov):
        for stlpec in range(pocet_stlpcov):
            if (riadok, stlpec) not in rohy:
                pocet_susedov = 0

                for smer in smery:
                    sused = (riadok+smer[0], stlpec+smer[1])

                    if 0 <= sused[0] <= pocet_riadkov - 1 and 0 <= sused[1] <= pocet_stlpcov - 1:
                        if svetielka[sused[0]][sused[1]] == "#":
                            pocet_susedov += 1

                if svetielka[riadok][stlpec] == "#":
                    if pocet_susedov not in {2, 3}:
                        zmena.append((riadok, stlpec))

                else:
                    if pocet_susedov == 3:
                        zmena.append((riadok, stlpec))

    for z in zmena:
        if svetielka[z[0]][z[1]] == "#":
            svetielka[z[0]][z[1]] = "."

        else:
            svetielka[z[0]][z[1]] = "#"

vysledok = 0
for riadok in range(pocet_riadkov):
    for stlpec in range(pocet_stlpcov):
        if svetielka[riadok][stlpec] == "#":
            vysledok += 1

print(vysledok)

# vysledok je 781
