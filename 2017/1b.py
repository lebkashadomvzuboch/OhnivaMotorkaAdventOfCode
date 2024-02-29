vysledok = 0
f = set()
r = []

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        r.append(int(riadok.strip()))

while True:
    for riadok in r:
        vysledok += riadok
        if vysledok in f:
            print(vysledok)
            quit()

        else:
            f.add(vysledok)

