risk = []
smery = ((1, 0), (0, 1), (-1, 0), (0, -1))
velke_cislo = 999999999999999

with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        risk.append([int(i) for i in riadok.strip()])


risk_ = risk.copy()
pocet_riadkov, pocet_stlpcov = len(risk), len(risk[0])

for i in range(1, 5):
    for riadok in range(pocet_riadkov):
        pridat = []
        for cislo in risk_[riadok]:
            if cislo + i == 10:
                pridat.append(1)
            elif cislo + i == 9:
                pridat.append(9)

            else:
                pridat.append((cislo+i) % 9)

        risk[riadok] = risk[riadok] + pridat

for i in range(1, 5):
    for riadok in range(pocet_riadkov):
        pridat = []

        for cislo in risk[riadok]:
            if cislo + i == 10:
                pridat.append(1)
            elif cislo + i == 9:
                pridat.append(9)

            else:
                pridat.append((cislo+i) % 9)

        risk.append(pridat)

for i in risk:
    t = ""
    for j in i:
        t += str(j)

    print(t)

pocet_riadkov *= 5
pocet_stlpcov *= 5


start, koniec = (0, 0), (pocet_riadkov-1, pocet_stlpcov-1)

navstivene = [[False for i in range(pocet_stlpcov)]
              for j in range(pocet_riadkov)]
vzdialenosti = [[velke_cislo for i in range(
    pocet_stlpcov)] for j in range(pocet_riadkov)]

vzdialenosti[0][0] = 0


def najmensia_vzdialenost(vzdialenosti, navsitvene):
    najmensie = velke_cislo
    najmensi_index = 0

    for riadok in range(pocet_riadkov):
        for stlpec in range(pocet_stlpcov):
            if not navsitvene[riadok][stlpec]:
                if vzdialenosti[riadok][stlpec] < najmensie:
                    najmensie = vzdialenosti[riadok][stlpec]
                    najmensi_index = (riadok, stlpec)

    return najmensi_index


def dijkstra(navstivene, vzdialenosti):

    for _ in range(pocet_riadkov*pocet_stlpcov):
        print(_)
        terajsie = najmensia_vzdialenost(vzdialenosti, navstivene)
        navstivene[terajsie[0]][terajsie[1]] = True

        if terajsie == koniec:
            return

        for smer in smery:
            sused = terajsie[0]+smer[0], terajsie[1]+smer[1]

            if 0 <= sused[0] < pocet_riadkov and 0 <= sused[1] < pocet_stlpcov:
                vzdialenosti[sused[0]][sused[1]] = min(
                    vzdialenosti[sused[0]][sused[1]], vzdialenosti[terajsie[0]][terajsie[1]]+risk[sused[0]][sused[1]])


dijkstra(navstivene, vzdialenosti)
print(vzdialenosti[koniec[0]][koniec[1]])

# vzdialenost je 2879
# exited with code=0 in 3583.828 seconds
# chcel som aj takyto approach, codee je hrozostrasny
