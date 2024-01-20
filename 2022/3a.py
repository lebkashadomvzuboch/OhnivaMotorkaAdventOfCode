vysledok = 0
abeceda = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        ruksak = riadok.strip()
        dlzka_ruksaku = len(ruksak)

        c = None
        for item in ruksak[:dlzka_ruksaku // 2]:
            for item_2 in ruksak[dlzka_ruksaku // 2:]:
                if item == item_2:
                    c = item

        vysledok += abeceda.index(c)


print(vysledok)

# vysledok je 8401
