cranes = None

with open("input_.txt", "r") as subor:
    while True:
        riadok = subor.readline().strip("\n")

        cislo = False
        for c in riadok:
            if c.isnumeric():
                cislo = True

        if cislo:
            break

        cranes_to_add = []

        for i in range(1, len(riadok), 4):
            if riadok[i] == " ":
                cranes_to_add.append(None)

            else:
                cranes_to_add.append(riadok[i])

        if cranes:
            for index, hodnota in enumerate(cranes_to_add):
                if hodnota:
                    cranes[index].append(hodnota)

        else:
            cranes = []
            for vec in cranes_to_add:
                if vec:
                    cranes.append([vec])
                else:
                    cranes.append([])

    subor.readline()

    for riadok in subor.readlines():
        info = riadok.strip()
        do = int(info.split(" to ")[1])
        od = int(info.split(" to ")[0].split(" from ")[1])
        pocet = int(info.split(" from ")[0].strip("move "))

        for i in range(pocet):
            cranes[do-1].insert(0, cranes[od-1].pop(0))

    s = ""
    for c in cranes:
        s += c[0]

    print(s)


# vysledok je QPJPLMNNR
