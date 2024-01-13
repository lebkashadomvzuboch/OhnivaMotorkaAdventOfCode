vysledok = 0

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        riadok = riadok.strip()
        vysledok += 2 + riadok.count("\"") + riadok.count("\\")

print(vysledok)

# vysledok je 2085, ovela krajsie
