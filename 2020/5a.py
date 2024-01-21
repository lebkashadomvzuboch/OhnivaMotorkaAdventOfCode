vysledok = 0

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        c1, c2 = riadok[0:7].replace("F", "0").replace(
            "B", "1"), riadok[7:].replace("L", "0").replace("R", "1")
        vysledok = max(vysledok, 8 * int(c1, 2) + int(c2, 2))

print(vysledok)

# vysledok je 842
