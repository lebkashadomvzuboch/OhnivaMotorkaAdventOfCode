vysledok = 0
with open("aoc/input.txt") as subor:
    for riadok in subor.readlines():
        sedi, su_posebe, samohlasky = True, False, 0
        for index, znak in enumerate(riadok.strip()):
            if znak in "aeiou":
                samohlasky += 1
            if index != 0:
                if riadok[index] == riadok[index-1]:
                    su_posebe = True
            
        for i in ("ab", "cd", "pq", "xy"):
            if i in riadok:
                sedi = False
        sedi = False if samohlasky < 3 else sedi
        sedi = False if not su_posebe else sedi
        vysledok += 1 if sedi else 0

print(vysledok)

# vysledok je 236
