vysledok = 0
musi_mat = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

with open("input.txt", "r") as subor:
    s = ""
    for riadok in subor.readlines():
        if riadok != "\n":
            s += riadok

        else:
            moze = True
            for m in musi_mat:
                if m not in s:
                    moze = False

            vysledok += 1 if moze else 0
            s = ''

    moze = True
    for m in musi_mat:
        if m not in s:
            moze = False

    vysledok += 1 if moze else 0


print(vysledok)

# vysledok je 213
