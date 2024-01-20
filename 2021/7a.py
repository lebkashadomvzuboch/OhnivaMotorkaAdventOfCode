import statistics
kraby = None

with open("input_.txt", "r") as subor:
    kraby = [int(i) for i in subor.readline().strip().split(",")]

median = statistics.median(kraby)

vysledok = 0
for krab in kraby:
    vysledok += abs(median - krab)

print(vysledok)

# vysledok je 355989
