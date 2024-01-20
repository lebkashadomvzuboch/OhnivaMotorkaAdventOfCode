stromy = []
smery = ((0, 1), (1, 0), (-1, 0), (0, -1))

with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        stromy.append([int(i) for i in riadok.strip()])

je_vidno = [[None for i in range(len(stromy[0]))] for i in range(len(stromy))]
pocet_riadkov, pocet_stlpcov = len(stromy), len(stromy[0])

for index_riadku, riadok in enumerate(stromy):
    for index_stlpca, cislo in enumerate(riadok):
        je_vidno_strom = False
        for smer in smery:
            kontrola = index_riadku + smer[0], index_stlpca + smer[1]
            if not (0 <= kontrola[0] < pocet_riadkov and 0 <= kontrola[1] < pocet_stlpcov):
                je_vidno_strom = True
                break

        if not je_vidno_strom:
            if index_stlpca != 0:
                if max(stromy[index_riadku][:index_stlpca]) < cislo:
                    je_vidno_strom = True

            if index_stlpca != pocet_stlpcov:
                if max(stromy[index_riadku][index_stlpca+1:]) < cislo:
                    je_vidno_strom = True

            if index_riadku != 0:
                if max([stromy[i][index_stlpca] for i in range(0, index_riadku)]) < cislo:
                    je_vidno_strom = True

            if index_riadku != pocet_riadkov:
                if max([stromy[i][index_stlpca] for i in range(index_riadku+1, pocet_riadkov)]) < cislo:
                    je_vidno_strom = True

        je_vidno[index_riadku][index_stlpca] = True if je_vidno_strom else False


vysledok = 0
for s in je_vidno:
    for c in s:
        vysledok += 1 if c else 0

print(vysledok)
# vysledok je 1533
