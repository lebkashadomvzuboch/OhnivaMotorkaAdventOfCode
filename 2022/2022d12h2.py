hory = []
smery = ((1, 0), (0, 1), (-1, 0), (0, -1))
velke_cislo = 99999
start = None
abeceda = "SabcdefghijklmnopqrstuvwxyzE"

with open("input_.txt", "r") as subor:
    for index_, riadok in enumerate(subor.readlines()):
        if "E" in riadok:
            start = index_, riadok.index("E")

        hory.append([i for i in riadok.strip()])


pocet_riadkov, pocet_stlpcov = len(hory), len(hory[0])

navstivene = [[False for i in range(pocet_stlpcov)]
              for j in range(pocet_riadkov)]
vzdialenosti = [[velke_cislo for i in range(
    pocet_stlpcov)] for j in range(pocet_riadkov)]

vzdialenosti[start[0]][start[1]] = 0


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
                if abeceda.index(hory[terajsie[0]][terajsie[1]]) - abeceda.index(hory[sused[0]][sused[1]]) < 2:
                    if hory[sused[0]][sused[1]] == "a":
                        print(vzdialenosti[terajsie[0]][terajsie[1]] + 1)
                        return
                    vzdialenosti[sused[0]][sused[1]] = min(
                        vzdialenosti[sused[0]][sused[1]], vzdialenosti[terajsie[0]][terajsie[1]]+1)


dijkstra(navstivene, vzdialenosti)

# vysledok je 354
# sikovne kopirovanie 2022/2021d15h1.py
