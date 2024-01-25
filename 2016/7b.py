import re
vysledok = 0


def prehladaj(vec):
    r = []
    for i in range(0, len(vec)-2):
        if vec[i] == vec[i+2] and vec[i+1] != vec[i+2]:
            r .append(f"{vec[i]}{vec[i+1]}{vec[i+2]}")

    return r


with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        result = re.split(r'(\[.*?\])', riadok)
        # milujem re

        vonkajsie, vnutorne = [], []

        for r in result:
            if r.startswith("["):
                vnutorne = vnutorne + prehladaj(r.strip("[]"))
            else:
                vonkajsie = vonkajsie + prehladaj(r)

        for von in vonkajsie:
            if f"{von[1]}{von[0]}{von[1]}" in vnutorne:
                vysledok += 1
                break


print(vysledok)

# vysledok je 258
