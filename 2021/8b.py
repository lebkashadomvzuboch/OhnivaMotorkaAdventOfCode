total = 0
originalne_cisla = {"nula": 0, "jeden": 1, "dva": 2, "tri": 3,
                    "stiry": 4, "pat": 5, "sest": 6, "sedem": 7, "osem": 8, "devat": 9}


def chyba_cislo(a, b):
    return (set(a) - set(b)).remove()


with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        cisla = {"a": None, "b": None, "c": None,
                 "d": None, "e": None, "f": None, "g": None}
        cisla_podla_slov = {"nula": None, "jeden": None, "dva": None, "tri": None,
                            "stiry": None, "pat": None, "sest": None, "sedem": None, "osem": None, "devat": None}

        udaje, vysledok = riadok.strip().split(" | ")
        udaje = udaje.split(" ")
        vysledok = vysledok.split(" ")

        for udaj in udaje:
            if len(udaj) == 2:
                cisla_podla_slov["jeden"] = udaj
            elif len(udaj) == 3:
                cisla_podla_slov["sedem"] = udaj
            elif len(udaj) == 4:
                cisla_podla_slov["stiry"] = udaj
            elif len(udaj) == 7:
                cisla_podla_slov["osem"] = udaj

        cisla["a"] = chyba_cislo(
            cisla_podla_slov["sedem"], cisla_podla_slov["jeden"])

        sestky = [slovo for slovo in udaje if len(slovo) == 6]
        patky = [slovo for slovo in udaje if len(slovo) == 5]

        for sestka in sestky:
            for pismeno in cisla_podla_slov["osem"]:
                if pismeno not in sestka and pismeno in cisla_podla_slov["jeden"]:
                    cisla_podla_slov["sest"] = sestka
                    cisla["c"] = pismeno
                    cisla["f"] = cisla_podla_slov["jeden"].strip(cisla["c"])
                    break

        for patka in patky:
            if cisla["c"] in patka and cisla["f"] in patka:
                cisla_podla_slov["tri"] = patka
            elif cisla["c"] in patka:
                cisla_podla_slov["dva"] = patka
            else:
                cisla_podla_slov["pat"] = patka

        for pismeno in cisla_podla_slov["sest"]:
            if pismeno not in cisla_podla_slov["pat"]:
                cisla["e"] = pismeno

        for sestka in sestky:
            if cisla["e"] not in sestka:
                cisla_podla_slov["devat"] = sestka

        for sestka in sestky:
            if sestka != cisla_podla_slov["devat"] and sestka != cisla_podla_slov["sest"]:
                cisla_podla_slov["nula"] = sestka

        for pismeno in cisla_podla_slov["devat"]:
            if pismeno not in cisla_podla_slov["tri"]:
                cisla["b"] = pismeno

        for pismeno in cisla_podla_slov["osem"]:
            if pismeno not in cisla_podla_slov["nula"]:
                cisla["d"] = pismeno

        for pismeno in cisla_podla_slov["osem"]:
            if pismeno != cisla["a"] and pismeno != cisla["e"] and pismeno not in cisla_podla_slov["stiry"]:
                cisla["g"] = pismeno

        text = ""
        for hadankove_cislo in vysledok:
            for key, value in cisla_podla_slov.items():
                t_v = list(value)
                t_h = list(hadankove_cislo)
                t_v.sort()
                t_h.sort()
                if t_v == t_h:
                    text += str(originalne_cisla[key])

        total += int(text)

print(total)

# take cudne risenie ale we ball
# vysledok je 1011823
