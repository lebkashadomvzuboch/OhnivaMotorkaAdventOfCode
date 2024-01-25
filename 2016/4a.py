vysledok = 0
abeceda = "abcdefghijklmnopqrstuvwxyz"

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        info = riadok.split("[")
        cislo = int(info[0].split("-")[-1])
        pismenka = info[1].strip("]\n")

        moze = True
        cisla = [info[0].count(p) for p in pismenka]

        for m in info[0]:
            if m.isalpha() and m not in pismenka:
                if info[0].count(m) > min(cisla):
                    moze = False

        for i in range(len(pismenka) - 1):
            if cisla[i] < cisla[i+1]:
                moze = False
                break

            elif cisla[i] == cisla[i+1]:
                if abeceda.index(pismenka[i]) > abeceda.index(pismenka[i+1]):
                    moze = False
                    break

        vysledok += cislo if moze else 0

print(vysledok)
# vysledok je 158835
