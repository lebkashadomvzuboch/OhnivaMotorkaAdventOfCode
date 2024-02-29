vysledok = 0

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        vysledok += int(riadok.strip())

print(vysledok)
