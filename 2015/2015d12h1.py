vysledok = 0
with open("input.txt", "r") as subor:
    udaj = subor.readline().strip()
    cislo = ""

    for znak in udaj:
        if znak == "-":
            cislo += znak
        if znak.isnumeric():
            cislo += znak
        else:
            if cislo not in ("", "-"):
                vysledok += int(cislo)
                cislo = ""

print(vysledok)

# vysledok je 111754
