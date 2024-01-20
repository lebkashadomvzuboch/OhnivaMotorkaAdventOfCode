morske_dno = []
kroky = 0
pohlo_sa = True

with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        morske_dno.append([i for i in riadok.strip()])

pocet_riadkov, pocet_stlpcov = len(morske_dno), len(morske_dno[0])


while pohlo_sa:
    p1, p2 = False, False
    kroky += 1

    treba_pohnut = []
    for riadok in range(pocet_riadkov):
        for stlpec in range(pocet_stlpcov):
            if morske_dno[riadok][stlpec] == ">":
                if stlpec == pocet_stlpcov-1:
                    if morske_dno[riadok][0] == ".":
                        treba_pohnut.append((riadok, stlpec))

                else:
                    if morske_dno[riadok][stlpec+1] == ".":
                        treba_pohnut.append((riadok, stlpec))

    p1 = True if len(treba_pohnut) > 0 else False

    for suradnice in treba_pohnut:
        morske_dno[suradnice[0]][suradnice[1]] = "."
        if suradnice[1] == pocet_stlpcov-1:
            morske_dno[suradnice[0]][0] = ">"
        else:
            morske_dno[suradnice[0]][suradnice[1]+1] = ">"

    treba_pohnut = []
    for riadok in range(pocet_riadkov):
        for stlpec in range(pocet_stlpcov):
            if morske_dno[riadok][stlpec] == "v":
                if riadok == pocet_riadkov-1:
                    if morske_dno[0][stlpec] == ".":
                        treba_pohnut.append((riadok, stlpec))

                else:
                    if morske_dno[riadok+1][stlpec] == ".":
                        treba_pohnut.append((riadok, stlpec))

    p2 = True if len(treba_pohnut) > 0 else False

    for suradnice in treba_pohnut:
        morske_dno[suradnice[0]][suradnice[1]] = "."
        if suradnice[0] == pocet_riadkov-1:
            morske_dno[0][suradnice[1]] = "v"
        else:
            morske_dno[suradnice[0]+1][suradnice[1]] = "v"

    pohlo_sa = p1 or p2


else:
    print(kroky)

# vysledok je 518
