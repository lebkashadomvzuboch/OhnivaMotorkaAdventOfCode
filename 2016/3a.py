vysledok = 0

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        cisla = [int(i.strip()) for i in riadok.strip().split(" ") if i.strip() != ""]
        cisla.sort()

        if cisla[0] + cisla[1] > cisla[2]:
            vysledok += 1

print(vysledok)

# vysledok je 1050
