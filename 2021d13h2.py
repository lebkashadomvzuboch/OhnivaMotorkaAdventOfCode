papier = []
bodky = []
pokiny = []


with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        if riadok.startswith("fold"):
            pokiny.append(riadok.strip())
        elif riadok != "\n":
            a, b = [int(i) for i in riadok.strip().split(",")]
            bodky.append((a, b))

nove_bodky = []
for pokin in pokiny:
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

    bodky = nove_bodky

# to precitam nejdem sa s tym babrat

sirka, vyska = 0, 0

for bodka in bodky:
    sirka = max(sirka, bodka[0])
    vyska = max(sirka, bodka[1])

mapa_na_print = [["." for i in range(sirka+1)] for j in range(vyska+1)]

for bodka in bodky:
    mapa_na_print[bodka[1]][bodka[0]] = "#"

for m in mapa_na_print:
    print(m)

# vysledok je HLBUBGFR
# prvy krat co vidim input co nie je cislo
