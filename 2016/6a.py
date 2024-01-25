prikazy = []

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        prikazy.append(riadok.strip())

pocet_pismeniek = len(prikazy[0])

vyskyt = [dict() for i in range(pocet_pismeniek)]

for prikaz in prikazy:
    for index_pismena, pismeno in enumerate(prikaz):
        if pismeno in vyskyt[index_pismena]:
            vyskyt[index_pismena][pismeno] += 1
        else:
            vyskyt[index_pismena][pismeno] = 1

vysledok = ""

for v in vyskyt:
    vysledok += max(v, key=v.get)

print(vysledok)

# vysledok je qqqluigu
