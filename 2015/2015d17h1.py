import itertools
nadoby = []
limit = 150
total = 0

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        nadoby.append(int(riadok.strip()))


def postup(nadoby, limit, total=0):
    for i in range(len(nadoby)):
        for moznost in itertools.combinations(nadoby, i):
            if sum(moznost) == limit:
                total += 1

    return total


print(postup(nadoby, limit))

# vysledok je 4372
