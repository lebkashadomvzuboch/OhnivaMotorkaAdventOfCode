chobotnice = []
smery = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
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


k = 0
nie_su_rovanke = True
while nie_su_rovanke:
    nie_su_rovanke = False
    k += 1
    uz_bolo = []
    for riadok in range(pocet_riadkov):
        for stlpec in range(pocet_stlpcov):
            chobotnice[riadok][stlpec] += 1

    for riadok in range(pocet_riadkov):
        for stlpec in range(pocet_stlpcov):
            if (riadok, stlpec) not in uz_bolo:
                if chobotnice[riadok][stlpec] > 9:
                    svieti(riadok, stlpec)

    for riadok in chobotnice:
        for chobotnica in riadok:
            if chobotnica != 0:
                nie_su_rovanke = True


print(k)

# vysledok je 337
