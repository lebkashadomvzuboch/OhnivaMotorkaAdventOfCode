mriezka = [[0 for i in range(1000)] for j in range(1000)]
vysledok = 0


with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        info = riadok.strip().split(" ")

        if info[0].startswith("toggle"):
            od = [int(i) for i in info[1].split(",")]
            do = [int(i) for i in info[3].split(",")]

            for x in range(od[0], do[0]+1):
                for y in range(od[1], do[1]+1):
                    mriezka[x][y] += 2

        elif info[0].startswith("turn"):
            od = [int(i) for i in info[2].split(",")]
            do = [int(i) for i in info[4].split(",")]

            if info[1].startswith("on"):
                for x in range(od[0], do[0]+1):
                    for y in range(od[1], do[1]+1):
                        mriezka[x][y] += 1

            else:
                for x in range(od[0], do[0]+1):
                    for y in range(od[1], do[1]+1):
                        if mriezka[x][y] > 0:
                            mriezka[x][y] -= 1

for a in range(1000):
    for b in range(1000):
        vysledok += mriezka[a][b]

print(vysledok)

# vysledok je 14687245
