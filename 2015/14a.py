soby = dict()
sekundy = 2503
vysledok = 0

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        info = riadok.split(" ")
        meno, rychlost, cas, oddych = info[0], int(
            info[3]), int(info[6]), int(info[13])

        soby[meno] = {"rychlost": rychlost, "pauza": cas, "oddych": oddych}

for sob in soby:
    zatial = sekundy // (soby[sob]["pauza"] + soby[sob]["oddych"])
    chyba = sekundy - (zatial * (soby[sob]["pauza"] + soby[sob]["oddych"]))

    prejdene = (zatial * soby[sob]["rychlost"] * soby[sob]["pauza"]) + (soby[sob]["rychlost"] *
                                                                        chyba if chyba < soby[sob]["pauza"] else soby[sob]["rychlost"] *
                                                                        soby[sob]["pauza"])

    vysledok = max(prejdene, vysledok)

print(vysledok)

# vysledok je 2696
