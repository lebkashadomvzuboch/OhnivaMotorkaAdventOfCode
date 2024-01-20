pokyny = []
pocet_riadkov, pocet_stlpcov = 0, 0

with open("input_.txt") as subor:
    for riadok in subor.readlines():
        info = riadok.strip().split(" -> ")
        zaciatok, koniec = [int(i) for i in info[0].split(",")], [
            int(i) for i in info[1].split(",")]

        pokyny.append((zaciatok, koniec))

        pocet_riadkov = max(zaciatok[0], koniec[0], pocet_riadkov)
        pocet_stlpcov = max(zaciatok[1], koniec[1], pocet_stlpcov)

morske_dno = [[0 for i in range(pocet_stlpcov+1)]
              for j in range(pocet_riadkov+1)]

for pokyn in pokyny:
    if pokyn[0][0] == pokyn[1][0]:
        do, od = max(pokyn[0][1], pokyn[1][1]), min(pokyn[0][1], pokyn[1][1])
        for i in range(od, do+1):
            morske_dno[pokyn[0][0]][i] += 1

    elif pokyn[0][1] == pokyn[1][1]:
        do, od = max(pokyn[0][0], pokyn[1][0]), min(pokyn[0][0], pokyn[1][0])
        for i in range(od, do+1):
            morske_dno[i][pokyn[0][1]] += 1

    elif abs(pokyn[0][0] - pokyn[1][0]) == abs(pokyn[0][1] - pokyn[1][1]):
        vektor_smeru = 1 if pokyn[0][0] < pokyn[1][0] else - \
            1, 1 if pokyn[0][1] < pokyn[1][1] else -1

        for i in range(abs(pokyn[0][0] - pokyn[1][0]) + 1):
            morske_dno[pokyn[0][0] + i * vektor_smeru[0]
                       ][pokyn[0][1] + i * vektor_smeru[1]] += 1


vysledok = 0
for m in morske_dno:
    for cislo in m:
        if cislo > 1:
            vysledok += 1
print(vysledok)

# vysledok je 20484
