podlaha = []
import copy

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        podlaha.append([i for i in riadok.strip()])


def skontroluj(podlaha, strazca, vyska, sirka):
    navstivene = set()
    je_cyklus = False
    obsadene = [[None for i in range(sirka)] for j in range(vyska)]

    smery = ((-1, 0), (0, 1), (1, 0), (0, -1))
    aktualny_smer = 0

    while True:
        ns = strazca[0] + smery[aktualny_smer][0], strazca[1] + smery[aktualny_smer][1]
        if not (-1 < ns[0] < vyska and -1 < ns[1] < sirka):
            break

        if (ns, aktualny_smer) in navstivene:
            je_cyklus = True
            break
        else:
            navstivene.add((ns, aktualny_smer))

        if podlaha[ns[0]][ns[1]] == "#":
            aktualny_smer = (aktualny_smer + 1) % 4
        
        else:
            obsadene[ns[0]][ns[1]] = "X"
            strazca = ns

    return je_cyklus

vyska, sirka = len(podlaha), len(podlaha[0])
STRAZCA = [None, None]

for i in range(vyska):
        for j in range(sirka):
            if podlaha[i][j] == "^":
                STRAZCA = [i, j]

vysledok = 0

for v in range(vyska):
    for s in range(sirka):
        print(v, s)
        if [v, s] == STRAZCA or podlaha[v][s] == "X":
            continue
        else:
            nova_podlaha = copy.deepcopy(podlaha)
            nova_podlaha[v][s] = "#"
            if skontroluj(nova_podlaha, STRAZCA, vyska, sirka):
                vysledok += 1


print(vysledok)
# vysledok je 1586

# da sa to optimalizovat:
    # davat prekazky len tam, kde prejde aj straznik