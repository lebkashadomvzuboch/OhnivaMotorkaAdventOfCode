navigacia = "R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3"

navigacia = navigacia.split(", ")
pozicia = 0, 0
smery = [["N", [1, 0]], ["E", [0, 1]], ["S", [-1, 0]], ["W", (0, -1)]] 
smer = 0
navstivene = set((0, 0))

for n in navigacia:
    if n.startswith("R"):
        smer = (smer + 1) % 4
    else:
        smer = (smer - 1) % 4

    for i in range(int(n.strip("RL"))):

        pozicia = pozicia[0] + smery[smer][1][0], pozicia[1] + smery[smer][1][1]

        if pozicia in navstivene:
            print(abs(pozicia[0]) + abs(pozicia[1]))
            quit()

        navstivene.add(pozicia)

    

# vysledok je 131
