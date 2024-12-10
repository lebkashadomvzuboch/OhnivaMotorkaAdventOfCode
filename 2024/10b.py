mapa = []

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        mapa.append([i for i in riadok.strip()])

vyska, sirka = len(mapa), len(mapa[0])
smery = ((1, 0), (0, 1), (-1, 0), (0, -1))

vysledky = []


def sprav_krok(v, s, cislo=0, policka=[]):
    if mapa[v][s] == "9":
        policka.append(1)
    for smer in smery:
        np = v+smer[0], s+smer[1]
        if -1 < np[0] < vyska and -1 < np[1] < sirka:
            if mapa[np[0]][np[1]] == str(int(cislo)+1):
                sprav_krok(np[0], np[1], str(int(cislo)+1), policka=policka)

    return policka

for v in range(vyska):
    for s in range(sirka):
        if mapa[v][s] == "0":
            vysledky.append(len(sprav_krok(v, s, 0, [])))

print(sum(vysledky))
# vysledok je 1326