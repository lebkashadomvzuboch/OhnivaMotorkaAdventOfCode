cykly = {20 + i*40 for i in range(6)}
vysledok = 0


with open("input_.txt", "r") as subor:
    cyklus = 0
    x = 1
    for riadok in subor.readlines():
        if riadok.startswith("noop"):
            cyklus += 1
            vysledok += x * cyklus if cyklus in cykly else 0

        else:
            cislo = int(riadok.strip().split(" ")[1])

            cyklus += 1
            vysledok += x * cyklus if cyklus in cykly else 0
            cyklus += 1
            vysledok += x * cyklus if cyklus in cykly else 0

            x += cislo


print(vysledok)

# vysledok je 14220
