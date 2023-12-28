papier = []
bodky = []
pokiny = []

sirka, vyska = 0, 0

with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        if riadok.startswith("fold"):
            pokiny.append(riadok.strip())
        elif riadok != "\n":
            a, b = [int(i) for i in riadok.strip().split(",")]
            sirka = max(a, sirka)
            vyska = max(b, vyska)
            bodky.append((a, b))

for pokin in pokiny[0:1]:
    info = pokin.split("=")
    smer, cislo = info[0][-1], int(info[1])

    nove_bodky = []

    if smer == "x":
        for bodka in bodky:
            if bodka[0] > cislo:
                nove_bodky.append((cislo - (bodka[0] - cislo), bodka[1]))

            else:
                nove_bodky.append(bodka)

    else:
        for bodka in bodky:
            if bodka[1] > cislo:
                nove_bodky.append((bodka[0], cislo - (bodka[1] - cislo)))

            else:
                nove_bodky.append(bodka)

    print(len(set(nove_bodky)))

# vysledok je 810
