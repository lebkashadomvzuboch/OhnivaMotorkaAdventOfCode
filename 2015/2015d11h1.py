heslo = "hxbxwxba"
abeceda = "abcdefghijklmnopqrstuvwxyz"


def zisti_dalsie_heslo(heslo):
    for index, pismeno in enumerate(heslo[::-1]):
        if pismeno != "z":
            heslo = list(heslo)
            heslo[len(heslo)-index -
                  1] = abeceda[abeceda.index(heslo[len(heslo)-index-1]) + 1]
            return "".join(p for p in heslo)

        else:
            heslo = list(heslo)
            heslo[len(heslo)-index -
                  1] = "a"


def zisti_ci_sedi(heslo):
    if "l" in heslo or "o" in heslo or "i" in heslo:
        return False

    pocet_troch, pocet_dvoch, overlapping_ = 0, 0, False

    for index, pismeno in enumerate(heslo):
        if index != len(heslo) - 1:
            if heslo[index+1] == pismeno and not overlapping_:
                pocet_dvoch += 1
                overlapping_ = True
            else:
                overlapping_ = False

    for index in range(len(heslo) - 2):
        a = abeceda.index(heslo[index])
        b = abeceda.index(heslo[index+1])
        c = abeceda.index(heslo[index + 2])
        if abeceda.index(heslo[index]) == abeceda.index(heslo[index+1]) - 1 == abeceda.index(heslo[index + 2]) - 2:
            pocet_troch += 1

    if pocet_troch > 0 and pocet_dvoch > 1:
        return True
    else:
        return False


while not zisti_ci_sedi(heslo):
    heslo = zisti_dalsie_heslo(heslo)
else:
    print(heslo)

# vysledok je hxbxxyzz
