vysledok = 0

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        pary = riadok.strip().split(",")
        prvy_par, druhy_par = [int(i) for i in pary[0].split(
            "-")], [int(i) for i in pary[1].split("-")]

        if prvy_par[0] <= druhy_par[0] <= prvy_par[1] or druhy_par[0] <= prvy_par[0] <= druhy_par[1]:
            vysledok += 1

print(vysledok)

# vysledok je 431
