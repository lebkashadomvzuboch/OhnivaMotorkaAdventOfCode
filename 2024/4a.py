krizovka, vysledok = [], 0

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        krizovka.append([i for i in riadok.strip()])

sirka, dlzka = len(krizovka[0]), len(krizovka)

smery = ((1, 0), (1, 1), (0, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1))

for riadok in range(dlzka):
    for stlpec in range(sirka):
        if krizovka[riadok][stlpec] == "X":
            for smer in smery:
                if -1 < riadok + smer[0]*3 < dlzka and -1 < stlpec + smer[1] * 3 < sirka:
                    kontrola = ""
                    for i in range(1, 4):
                        kontrola += krizovka[riadok+smer[0]*i][stlpec+smer[1]*i]

                    if kontrola == "MAS":
                        vysledok += 1

print(vysledok)
# vysledok je 2560

