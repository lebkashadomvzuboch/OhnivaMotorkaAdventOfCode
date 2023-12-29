risk = []
smery = ((1, 0), (0, 1), (-1, 0), (0, -1))
velke_cislo = 999999999999999

with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        risk.append([int(i) for i in riadok.strip()])


pocet_riadkov, pocet_stlpcov = len(risk), len(risk[0])
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
        terajsie = najmensia_vzdialenost(vzdialenosti, navstivene)
        navstivene[terajsie[0]][terajsie[1]] = True

        for smer in smery:
            sused = terajsie[0]+smer[0], terajsie[1]+smer[1]

            if 0 <= sused[0] < pocet_riadkov and 0 <= sused[1] < pocet_stlpcov:
                vzdialenosti[sused[0]][sused[1]] = min(
                    vzdialenosti[sused[0]][sused[1]], vzdialenosti[terajsie[0]][terajsie[1]]+risk[sused[0]][sused[1]])

        if terajsie == koniec:
            return


dijkstra(navstivene, vzdialenosti)
print(vzdialenosti[koniec[0]][koniec[1]])

# vysledok je 540
