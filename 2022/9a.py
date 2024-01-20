hlava, chvost = [0, 0], [0, 0]
pozicie = set()
smery = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        smer, nasobok = riadok.strip().split(" ")

        for i in range(int(nasobok)):
            hlava[0] += smery[smer][0]
            hlava[1] += smery[smer][1]

            if abs(hlava[0] - chvost[0]) + abs(hlava[1] - chvost[1]) == 3:
                chvost[0] += 1 if hlava[0] > chvost[0] else -1
                chvost[1] += 1 if hlava[1] > chvost[1] else -1

            elif abs(hlava[0] - chvost[0]) == 2 or abs(hlava[1] - chvost[1]) == 2:
                chvost[0] += smery[smer][0]
                chvost[1] += smery[smer][1]

            pozicie.add(tuple(chvost))


print(len(pozicie))
# vysledok je 6470
