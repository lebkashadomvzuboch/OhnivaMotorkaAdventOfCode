vysledok = 0

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        info = riadok.strip().split(": ")
        info_2 = info[0].split(" ")
        info_3 = info_2[0].split("-")

        if (info[1][int(info_3[0]) - 1] == info_2[1]) ^ (info[1][int(info_3[1]) - 1] == info_2[1]):
            vysledok += 1

print(vysledok)

# vysledok je 245
