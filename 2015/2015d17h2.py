import itertools
nadoby = []
limit = 150
total = 0

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        nadoby.append(int(riadok.strip()))


def postup(nadoby, limit):
    for i in range(len(nadoby)):
        total = 0
        for moznost in itertools.combinations(nadoby, i):
            if sum(moznost) == limit:
                total += 1

        if total > 0:
            print(total)
            return

    return total


postup(nadoby, limit)
# vysledok je 4
