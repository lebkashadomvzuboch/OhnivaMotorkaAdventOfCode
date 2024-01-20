kraby = None

with open("input_.txt", "r") as subor:
    kraby = [int(i) for i in subor.readline().strip().split(",")]

najlepsie = 999999999999999999999999999999999999999999

for cislo in range(min(kraby), max(kraby)):
    cena = 0
    for krab in kraby:
        cena += abs(krab - cislo) * (abs(krab - cislo) + 1) / 2
    najlepsie = min(cena, najlepsie)

print(najlepsie)


# vysledok je 102245489
