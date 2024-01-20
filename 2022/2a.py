vysledok = 0
with open("input_.txt", "r") as subor:
    temp = 0
    for riadok in subor.readlines():
        elf, ty = riadok.strip().split(" ")

        vysledok += 1 if ty == "X" else 2 if ty == "Y" else 3

        if ty == "X":
            vysledok += 3 if elf == "A" else 6 if elf == "C" else 0

        elif ty == "Y":
            vysledok += 3 if elf == "B" else 6 if elf == "A" else 0

        else:
            vysledok += 3 if elf == "C" else 6 if elf == "B" else 0


print(vysledok)

# vysledok je 10595
