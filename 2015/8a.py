vysledok = 0

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        riadok = riadok.strip()
        t = 2
        for index, character in enumerate(riadok):
            if character == "\\":
                if riadok[index+1] == "x":
                    t += 3
                else:
                    if riadok[index+1] != "\\":
                        t += 1

        vysledok += t

print(vysledok+1)

# vysledok je 1350 chyba \n na konci inputu
