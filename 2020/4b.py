vysledok = 0
musi_mat = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def porzri(pas):
    moze_dalej = True
    for m in musi_mat:
        if m not in pas:
            moze_dalej = False
    if not moze_dalej:
        return False

    if not 1920 <= int(pas["byr"]) <= 2002:
        return False

    if not 2010 <= int(pas["iyr"]) <= 2020:
        return False

    if not 2020 <= int(pas["eyr"]) <= 2030:
        return False

    cislo = ""
    koncovka = ""

    for pismeno in pas["hgt"]:
        if pismeno.isnumeric():
            cislo += pismeno
        else:
            koncovka += pismeno

    if koncovka == "cm":
        if not 150 <= int(cislo) <= 193:
            return False
    else:
        if not 59 <= int(cislo) <= 76:
            return False

    mozne_byt_hcl = True

    if not pas["hcl"].startswith("#"):
        mozne_byt_hcl = False

    if len(pas["hcl"]) != 7:
        mozne_byt_hcl = False

    for pismeno in pas["hcl"][1:]:
        if pismeno not in "0123456789abcdef":
            mozne_byt_hcl = False

    if not mozne_byt_hcl:
        return False

    if pas["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False

    if not pas["pid"].isnumeric():
        return False

    if not len(pas["pid"]) == 9:
        return False

    return True


with open("input.txt", "r") as subor:
    s = {}
    for riadok in subor.readlines():
        if riadok != "\n":
            for par in riadok.strip().split(" "):
                info = par.split(":")
                s[info[0]] = info[1]

        else:
            vysledok += 1 if porzri(s) else 0
            s = {}

    vysledok += 1 if porzri(s) else 0


print(vysledok)

# vysledok je 147
vysledok = 0
musi_mat = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def porzri(pas):
    moze_dalej = True
    for m in musi_mat:
        if m not in pas:
            moze_dalej = False
    if not moze_dalej:
        return False

    if not 1920 <= int(pas["byr"]) <= 2002:
        return False

    if not 2010 <= int(pas["iyr"]) <= 2020:
        return False

    if not 2020 <= int(pas["eyr"]) <= 2030:
        return False

    cislo = ""
    koncovka = ""

    for pismeno in pas["hgt"]:
        if pismeno.isnumeric():
            cislo += pismeno
        else:
            koncovka += pismeno

    if koncovka == "cm":
        if not 150 <= int(cislo) <= 193:
            return False
    else:
        if not 59 <= int(cislo) <= 76:
            return False

    mozne_byt_hcl = True

    if not pas["hcl"].startswith("#"):
        mozne_byt_hcl = False

    if len(pas["hcl"]) != 7:
        mozne_byt_hcl = False

    for pismeno in pas["hcl"][1:]:
        if pismeno not in "0123456789abcdef":
            mozne_byt_hcl = False

    if not mozne_byt_hcl:
        return False

    if pas["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False

    if not pas["pid"].isnumeric():
        return False

    if not len(pas["pid"]) == 9:
        return False

    return True


with open("input.txt", "r") as subor:
    s = {}
    for riadok in subor.readlines():
        if riadok != "\n":
            for par in riadok.strip().split(" "):
                info = par.split(":")
                s[info[0]] = info[1]

        else:
            vysledok += 1 if porzri(s) else 0
            s = {}

    vysledok += 1 if porzri(s) else 0


print(vysledok)

# vysledok je 147
