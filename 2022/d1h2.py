vysledok = []
with open("input_.txt", "r") as subor:
    temp = 0
    for riadok in subor.readlines():
        if riadok == "\n":
            vysledok.sort()
            if len(vysledok) < 3:
                vysledok.append(temp)

            elif temp > vysledok[0]:
                vysledok[0] = temp

            temp = 0

        else:
            temp += int(riadok.strip())


print(sum(vysledok))

# vysledok je 208567
