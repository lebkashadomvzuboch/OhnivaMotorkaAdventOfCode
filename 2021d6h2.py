pocet_dni = 256
rybky = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}


with open("input_.txt") as subor:
    for i in subor.readline().strip().split(","):
        rybky[int(i)] += 1


for i in range(pocet_dni):
    nove_rybky = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for cislo_rybky in rybky:
        if cislo_rybky == 0:
            nove_rybky[6] += rybky[cislo_rybky]
            nove_rybky[8] += rybky[cislo_rybky]

        else:
            nove_rybky[cislo_rybky - 1] += rybky[cislo_rybky]

    rybky = nove_rybky.copy()

print(sum(rybky.values()))

# toto je take clean riesenie ze som len zmenil hodnotu jednej premennej
# vysledok je 1705008653296
