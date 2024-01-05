lano = [[0, 0] for i in range(10)]
pozicie = set()
smery = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}

with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        smer, nasobok = riadok.strip().split(" ")

        for i in range(int(nasobok)):
            for i in range(10):
                if i == 0:
                    lano[0][0] += smery[smer][0]
                    lano[0][1] += smery[smer][1]

                else:
                    hlava = lano[i-1]
                    chvost = lano[i]

                    if abs(hlava[0] - chvost[0]) + abs(hlava[1] - chvost[1]) >= 3:
                        if abs(hlava[0] - chvost[0]) == 1:
                            chvost[0] = hlava[0]
                        else:
                            if hlava[0] > chvost[0]:
                                chvost[0] = hlava[0] - 1
                            else:
                                chvost[0] = hlava[0] + 1

                        if abs(hlava[1] - chvost[1]) == 1:
                            chvost[1] = hlava[1]
                        else:
                            if hlava[1] > chvost[1]:
                                chvost[1] = hlava[1] - 1
                            else:
                                chvost[1] = hlava[1] + 1

                    elif abs(hlava[0] - chvost[0]) == 2 or abs(hlava[1] - chvost[1]) == 2:
                        if abs(hlava[0] - chvost[0]) == 2:
                            if hlava[0] > chvost[0]:
                                chvost[0] += 1
                            else:
                                chvost[0] -= 1

                        elif abs(hlava[1] - chvost[1]) == 2:
                            if hlava[1] > chvost[1]:
                                chvost[1] += 1
                            else:
                                chvost[1] -= 1

                    if i == 9:
                        pozicie.add(tuple(chvost))

print(len(pozicie))
# vysledok je 2658
# trvalo to dost dlho ale nevzdal som sa
# we ball
