vysledok = 0
with open("input_.txt", "r") as subor:
    temp = 0
    for riadok in subor.readlines():
        elf, ty = riadok.strip().split(" ")

        vysledok += 0 if ty == "X" else 3 if ty == "Y" else 6

        if elf == "A":
            vysledok += 3 if ty == "X" else 1 if ty == "Y" else 2

        elif elf == "B":
            vysledok += 1 if ty == "X" else 2 if ty == "Y" else 3

        else:
            vysledok += 2 if ty == "X" else 3 if ty == "Y" else 1


print(vysledok)

# vysledok je 9541
