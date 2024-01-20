chobotnice = []
smery = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
pocet_svieteni = 0
uz_bolo = []

pocet_riadkov, pocet_stlpcov = 10, 10

with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        chobotnice.append([int(i) for i in riadok.strip()])


def svieti(riadok, stlpec):
    if (riadok, stlpec) not in uz_bolo:
        uz_bolo.append((riadok, stlpec))
        chobotnice[riadok][stlpec] = 0

        for smer in smery:
            if 0 <= riadok + smer[0] < pocet_riadkov and 0 <= stlpec + smer[1] < pocet_stlpcov:
                p1 = True if chobotnice[riadok+smer[0]
                                        ][stlpec+smer[1]] != 0 else False
                p2 = True if chobotnice[riadok+smer[0]
                                        ][stlpec+smer[1]] not in uz_bolo else False

                if p1:
                    chobotnice[riadok+smer[0]][stlpec+smer[1]] += 1

                    if chobotnice[riadok+smer[0]][stlpec+smer[1]] > 9:
                        svieti(riadok+smer[0], stlpec+smer[1])


for i in range(100):
    uz_bolo = []
    for riadok in range(pocet_riadkov):
        for stlpec in range(pocet_stlpcov):
            chobotnice[riadok][stlpec] += 1

    for riadok in range(pocet_riadkov):
        for stlpec in range(pocet_stlpcov):
            if (riadok, stlpec) not in uz_bolo:
                if chobotnice[riadok][stlpec] > 9:
                    svieti(riadok, stlpec)

    for c in chobotnice:
        for l in c:
            if l == 0:
                pocet_svieteni += 1


print(pocet_svieteni)

# vysledok je 1655
# haha test input bol 1656, len o 1 menej
