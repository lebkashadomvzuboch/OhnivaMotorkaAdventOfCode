with open("input_.txt", "r") as subor:
    cyklus = 0
    sprite = 2
    pozicia = 0
    s = ""

    for riadok in subor.readlines():
        if riadok.startswith("noop"):
            cyklus += 1
            pozicia += 1
            s += "#" if pozicia in {sprite-1, sprite, sprite+1} else "."

            if cyklus % 40 == 0:
                print(s)
                s = ""
                pozicia = 0

        else:
            cislo = int(riadok.strip().split(" ")[1])

            cyklus += 1
            pozicia += 1
            s += "#" if pozicia in {sprite-1, sprite, sprite+1} else "."

            if cyklus % 40 == 0:
                print(s)
                s = ""
                pozicia = 0

            cyklus += 1
            pozicia += 1
            s += "#" if pozicia in {sprite-1, sprite, sprite+1} else "."

            if cyklus % 40 == 0:
                print(s)
                s = ""
                pozicia = 0

            sprite += cislo


# vysledok je ZRARLFZU
