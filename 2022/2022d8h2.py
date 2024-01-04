stromy = []
smery = ((0, 1), (1, 0), (-1, 0), (0, -1))
vysledok = 0


with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        stromy.append([int(i) for i in riadok.strip()])

je_vidno = [[None for i in range(len(stromy[0]))] for i in range(len(stromy))]
pocet_riadkov, pocet_stlpcov = len(stromy), len(stromy[0])

v = 0
for index_riadku, riadok in enumerate(stromy):
    for index_stlpca, cislo in enumerate(riadok):
        temp = 1
        for smer in smery:
            kontrola = [index_riadku + smer[0], index_stlpca + smer[1]]

            if 0 <= kontrola[0] < pocet_riadkov and 0 <= kontrola[1] < pocet_riadkov:
                padlo = False
                pocet_pohybov = 0
                while 0 <= kontrola[0] < pocet_riadkov and 0 <= kontrola[1] < pocet_stlpcov:
                    if cislo > stromy[kontrola[0]][kontrola[1]]:
                        pocet_pohybov += 1
                        kontrola[0] += smer[0]
                        kontrola[1] += smer[1]
                    else:
                        padlo = True
                        break

                temp *= pocet_pohybov if not padlo else pocet_pohybov + 1

            else:
                temp *= 0
                break

        vysledok = max(vysledok, temp)

print(vysledok)
# vysledok je 345744
