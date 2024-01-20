ty = {"mana": 500, "health": 50, "armor": 0}
boss = {"health": 71, "damage": 10}
vysledok = 999999

utoky = {"M": {"mana": 53, "damage": 4},
         "D": {"mana": 73, "damage": 2, "heal": 2},
         "S": {"mana": 113, "armor": 7, "duration": 6},
         "P": {"mana": 173, "damage": 3, "duration": 6},
         "R": {"mana": 229, "recharge": 101, "duration": 5}
         }

minute_many = []


def hladac(ty, boss, minuta_mana, efekty, tvoj_turn, uz_bolo=[]):
    if tvoj_turn:
        ty["health"] -= 1

    if efekty != dict():
        vymazat = []
        for efekt in efekty:
            if efekt == "S":
                ty["armor"] = utoky["S"]["armor"]

            elif efekt == "R":
                ty["mana"] += utoky["R"]["recharge"]

            elif efekt == "P":
                boss["health"] -= utoky["P"]["damage"]

            efekty[efekt] -= 1
            if efekty[efekt] == 0:
                if efekt == "S":
                    ty["armor"] = 0
                vymazat.append(efekt)

        for v in vymazat:
            del efekty[v]

    if boss["health"] <= 0:
        minute_many.append(minuta_mana)
        return

    if ty["health"] <= 0:
        return False

    if ty["mana"] < 53:
        return False

    if tvoj_turn:
        for kuzlo in utoky:
            if kuzlo not in efekty:
                if kuzlo == "M":
                    nove_efekty = efekty.copy()
                    hladac({"mana": ty["mana"] - utoky[kuzlo]["mana"], "health": ty["health"], "armor": ty["armor"]}, {
                        "health": boss["health"] - utoky[kuzlo]["damage"], "damage": boss["damage"]}, minuta_mana+utoky[kuzlo]["mana"], nove_efekty, False, uz_bolo+[kuzlo])

                elif kuzlo == "D":
                    nove_efekty = efekty.copy()
                    hladac({"mana": ty["mana"] - utoky[kuzlo]["mana"], "health": min(14, ty["health"] + utoky[kuzlo]["heal"]), "armor": ty["armor"]}, {
                        "health": boss["health"] - utoky[kuzlo]["damage"], "damage": boss["damage"]}, minuta_mana+utoky[kuzlo]["mana"], nove_efekty, False, uz_bolo+[kuzlo])

                elif kuzlo == "S":
                    nove_efekty = efekty.copy()
                    nove_efekty[kuzlo] = utoky[kuzlo]["duration"]
                    hladac({"mana": ty["mana"] - utoky[kuzlo]["mana"], "health": ty["health"], "armor": ty["armor"] + utoky[kuzlo]["armor"]}, {
                        "health": boss["health"], "damage": boss["damage"]}, minuta_mana+utoky[kuzlo]["mana"], nove_efekty, False, uz_bolo+[kuzlo])

                elif kuzlo == "P":
                    nove_efekty = efekty.copy()
                    nove_efekty[kuzlo] = utoky[kuzlo]["duration"]
                    hladac({"mana": ty["mana"] - utoky[kuzlo]["mana"], "health": ty["health"], "armor": ty["armor"]}, {
                        "health": boss["health"], "damage": boss["damage"]}, minuta_mana+utoky[kuzlo]["mana"], nove_efekty, False, uz_bolo+[kuzlo])

                elif kuzlo == "R":
                    nove_efekty = efekty.copy()
                    nove_efekty[kuzlo] = utoky[kuzlo]["duration"]
                    hladac({"mana": ty["mana"] - utoky[kuzlo]["mana"], "health": ty["health"], "armor": ty["armor"]}, {
                        "health": boss["health"], "damage": boss["damage"]}, minuta_mana+utoky[kuzlo]["mana"], nove_efekty, False, uz_bolo+[kuzlo])

    else:
        hladac({"mana": ty["mana"], "health": ty["health"] - max(boss["damage"] - ty["armor"], 1),
                "armor": ty["armor"]}, {"health": boss["health"], "damage": boss["damage"]}, minuta_mana, efekty, True, uz_bolo)

    return


hladac(ty, boss, 0, dict(), True)

print(min(minute_many))

# vysledok je 1937
# za 20 s som na to prisiel
