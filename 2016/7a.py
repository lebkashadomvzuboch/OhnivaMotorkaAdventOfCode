import re
vysledok = 0


def prehladaj(vec):
    r = False
    for i in range(0, len(vec)-3):
        if vec[i] == vec[i+3] and vec[i+1] == vec[i+2] and vec[i] != vec[i+1]:
            r = True
            break

    return r


with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        result = re.split(r'(\[.*?\])', riadok)

        # milujem re

        moze, nemoze = False, False

        for r in result:
            if r.startswith("["):
                if not nemoze:
                    nemoze = prehladaj(r.strip("[]"))
            else:
                if not moze:
                    moze = prehladaj(r)

        if not nemoze:
            if moze:
                vysledok += 1

print(vysledok)

# vysledok je 105
