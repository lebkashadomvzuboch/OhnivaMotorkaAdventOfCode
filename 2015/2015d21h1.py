import itertools
obchod = {}
kategorie = {}
boss = [109, 8, 2]
ty = [100, 0, 0]

# hp, dmg, armr

with open("input.txt", "r") as subor:
    aktualny_item, meno = {}, None
    for riadok in subor.readlines():
        if ":" in riadok:
            meno = riadok.split(": ")[0]

        elif riadok != "\n":
            info = [i.strip() for i in riadok.split("  ")]
            obchod[info[0]] = [int(i) for i in info[1:] if i != ""]

            if meno in kategorie:
                kategorie[meno].append(info[0])
            else:
                kategorie[meno] = [info[0]]


def suboj(ty, nepriatel):
    tvoj_damage = ty[1] - nepriatel[2] if ty[1] > nepriatel[2] else 1
    nepriatelov_damage = nepriatel[1] - ty[2] if nepriatel[1] > ty[2] else 1

    if ty[0] / nepriatelov_damage >= nepriatel[0] / tvoj_damage:
        return True

    return False


moznosti = []

for zbran, brnenie, prsten in itertools.product(kategorie["Weapons"], [None] + kategorie["Armor"], itertools.combinations([None] + [None] + kategorie["Rings"], r=2)):
    moznosti.append([zbran, brnenie, prsten[0], prsten[1]])

min_cena = 999999

for moznost in moznosti:
    cena, brnenie, damage = 0, 0, 0

    for vec in moznost:
        if vec:
            cena += obchod[vec][0]
            damage += obchod[vec][1]
            brnenie += obchod[vec][2]

    if suboj([ty[0], damage, brnenie], boss):
        min_cena = min(cena, min_cena)

print(min_cena)

# vysledok je 111
