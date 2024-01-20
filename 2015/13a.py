import itertools

ludia_hodnoty = dict()

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        info = riadok.strip().strip(".").split(" ")
        osoba1, zisk, cislo, osoba2 = info[0], info[2], int(info[3]), info[10]

        if osoba1 in ludia_hodnoty:
            ludia_hodnoty[osoba1][osoba2] = cislo if zisk == "gain" else -cislo
        else:
            ludia_hodnoty[osoba1] = {
                osoba2: cislo if zisk == "gain" else -cislo}


ludia = set(ludia_hodnoty)
moznosti_usadenia = set(itertools.permutations(ludia))

vysledok = 0

for moznost in moznosti_usadenia:
    temp = 0
    for index, clovek in enumerate(moznost):
        if index != len(ludia) - 1:
            temp += ludia_hodnoty[clovek][moznost[index+1]]
            temp += ludia_hodnoty[moznost[index+1]][clovek]
        else:
            temp += ludia_hodnoty[clovek][moznost[0]]
            temp += ludia_hodnoty[moznost[0]][clovek]

    vysledok = max(vysledok, temp)

print(vysledok)

# vysledok je 733
