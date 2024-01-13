cislo = 1113122113

def uprac(cislo):

    nove_cislo, aktualne_cislo, pocet_aktualnych_cisel = [], str(cislo)[0], 1

    for znak in str(cislo)[1:]:
        if znak == aktualne_cislo:
            pocet_aktualnych_cisel += 1

        else:
            nove_cislo.append([int(aktualne_cislo), pocet_aktualnych_cisel])
            aktualne_cislo = znak
            pocet_aktualnych_cisel = 1

    nove_cislo.append([int(aktualne_cislo), pocet_aktualnych_cisel])

    return nove_cislo


for i in range(50):
    rozumny_tvar = uprac(cislo)
    novy_tvar = ""
    for set_cisel in rozumny_tvar:
        novy_tvar += f"{set_cisel[1]}{set_cisel[0]}"

    cislo = novy_tvar

print(len(str(cislo)))

# vysledok je 360154
