vysledok = 0
with open("input_.txt", "r") as subor:
    temp = 0
    for riadok in subor.readlines():
        if riadok == "\n":
            vysledok = max(vysledok, temp)
            temp = 0
        else:
            temp += int(riadok.strip())


print(vysledok)

# vysledok je 70509
