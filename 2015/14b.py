soby = dict()
sekundy = 2503
vysledok = 0

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        info = riadok.split(" ")
        meno, rychlost, cas, oddych = info[0], int(
            info[3]), int(info[6]), int(info[13])

        soby[meno] = {"rychlost": rychlost, "pauza": cas,
                      "oddych": oddych, "bezi": True, "cas akcie": 0, "vzdialenost": 0}

skore = {sob: 0 for sob in soby}


def zisti_body(cosi):
    najviac_bodov = 0
    for sob in cosi:
        najviac_bodov = max(cosi[sob]["vzdialenost"], najviac_bodov)

    prvy = []
    for sob in cosi:
        if cosi[sob]["vzdialenost"] == najviac_bodov:
            prvy.append(sob)

    return prvy


for sekunda in range(sekundy):
    for sob in soby:
        soby[sob]["cas akcie"] += 1
        if soby[sob]["bezi"]:
            soby[sob]["vzdialenost"] += soby[sob]["rychlost"]
            if soby[sob]["pauza"] == soby[sob]["cas akcie"]:
                soby[sob]["bezi"] = False
                soby[sob]["cas akcie"] = 0

        else:
            if soby[sob]["oddych"] == soby[sob]["cas akcie"]:
                soby[sob]["bezi"] = True
                soby[sob]["cas akcie"] = 0

    for prvy in zisti_body(soby):
        skore[prvy] += 1


print(max(skore.values()))

# vysledok je 1084
