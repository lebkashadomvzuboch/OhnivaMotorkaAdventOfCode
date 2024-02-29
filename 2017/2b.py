pismena = []

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        pismena.append(riadok.strip())

for p in pismena:
    for druhe_p in pismena:
        pocet_zlych = 0
         
        for i in range(len(p)):
            if p[i] != druhe_p[i]:
                pocet_zlych += 1

        if pocet_zlych == 1:
            print(p)

# vysledok je nvosmkcdtdbfhyxsphzgraljq
# nvosmkcdtdbfhyxsphzgrraljq
# nvosmkcdtdbfhyxsphzgeraljq
