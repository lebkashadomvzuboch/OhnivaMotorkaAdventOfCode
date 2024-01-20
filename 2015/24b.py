import itertools
import math
baliky = None

with open("input.txt", "r") as subor:
    baliky = [int(i.strip()) for i in subor.readlines()]

vaha = sum(baliky) // 4
baliky.sort(reverse=True)


def hladac():
    for i in range(1, len(baliky)-1):
        for c in itertools.combinations(baliky, i):
            if sum(c) == vaha:
                print(math.prod(c))
                return


hladac()

# vysledok je 74850409
