prikazy = []
hodnoty = {"a": 1, "b": 0}
cislo_prikazu = 0

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        prikazy.append(riadok.strip())


while 0 <= cislo_prikazu <= len(prikazy) - 1:
    if prikazy[cislo_prikazu].startswith("hlf"):
        info = prikazy[cislo_prikazu].split(" ")
        hodnoty[info[1]] //= 2
        cislo_prikazu += 1

    elif prikazy[cislo_prikazu].startswith("tpl"):
        info = prikazy[cislo_prikazu].split(" ")
        hodnoty[info[1]] *= 3
        cislo_prikazu += 1

    elif prikazy[cislo_prikazu].startswith("inc"):
        info = prikazy[cislo_prikazu].split(" ")
        hodnoty[info[1]] += 1
        cislo_prikazu += 1

    elif prikazy[cislo_prikazu].startswith("jmp"):
        info = prikazy[cislo_prikazu].split(" ")
        o_kolko = int(info[1])
        cislo_prikazu += o_kolko

    elif prikazy[cislo_prikazu].startswith("jie"):
        info = prikazy[cislo_prikazu].split(", ")
        info_2 = info[0].split(" ")
        if hodnoty[info_2[1]] % 2 == 0:
            o_kolko = int(info[1])
            cislo_prikazu += o_kolko
        else:
            cislo_prikazu += 1

    elif prikazy[cislo_prikazu].startswith("jio"):
        info = prikazy[cislo_prikazu].split(", ")
        info_2 = info[0].split(" ")
        if hodnoty[info_2[1]] == 1:
            o_kolko = int(info[1])
            cislo_prikazu += o_kolko
        else:
            cislo_prikazu += 1


print(hodnoty["b"])

# vysledok je 334
# len som zmenil 0 na 1
