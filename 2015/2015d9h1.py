import itertools
cesty_do_miest = dict()
vysledok = 99999


with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        info = riadok.strip().split(" to ")
        druhe_info = info[1].split(" = ")

        if info[0] in cesty_do_miest:
            cesty_do_miest[info[0]][druhe_info[0]] = int(druhe_info[1])
        else:
            cesty_do_miest[info[0]] = {druhe_info[0]: int(druhe_info[1])}

        if druhe_info[0] in cesty_do_miest:
            cesty_do_miest[druhe_info[0]][info[0]] = int(druhe_info[1])
        else:
            cesty_do_miest[druhe_info[0]] = {info[0]: int(druhe_info[1])}


vsetky_miesta = set(cesty_do_miest.keys())

for moznost in tuple(itertools.permutations(vsetky_miesta)):
    temp = 0
    minule_mesto = moznost[0]
    for mesto in moznost[1:]:
        temp += cesty_do_miest[minule_mesto][mesto]
        minule_mesto = mesto

    vysledok = min(vysledok, temp)

print(vysledok)

# vysledok je 117
