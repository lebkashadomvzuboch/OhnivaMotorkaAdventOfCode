import copy
# 2016/11

pocet = 4
poschodia = {0: ["HM", "LM"], 1: ["HG"], 2: ["LG"], 3: []}
kde_je_vytah = 0
vysledky = set()
uz_bolo = dict()

def sprav_kolo(poschodia, kde_je_vytah, vytah=[], kolo=0, ide_hore=False):
    if vysledky:
        if kolo > min(vysledky):
            return
    if kde_je_vytah > 3 or kde_je_vytah < 0:
        return

    poschodia[kde_je_vytah] = poschodia[kde_je_vytah] + vytah

    minule = None
    if ide_hore:
        minule = kde_je_vytah - 1
    else:
        minule = kde_je_vytah + 1

    poschodia[minule] = [i for i in poschodia[minule] if i not in vytah and i]
    k = str(poschodia.values())


    if k in uz_bolo and uz_bolo[k] <= kolo:
        return
    else:
        uz_bolo[k] = kolo


    if len(poschodia[3]) == 4:
        vysledky.add(kolo)

    else:
        legalne = True
        for poschodie in poschodia:
            for vec in poschodia[poschodie]:
                if vec[-1] == "M":
                    if f"{vec[0]}G" not in poschodia[poschodie]:
                        for druha_vec in poschodia[poschodie]:
                            if druha_vec[-1] == "G":
                                legalne = False

        pocet_veci = len(poschodia[kde_je_vytah])
        if legalne and pocet_veci > 0:
            for vec in range(pocet_veci):
                vc = poschodia[kde_je_vytah][vec]
                sprav_kolo(copy.deepcopy(poschodia), kde_je_vytah-1, [vc], kolo+1)
                sprav_kolo(copy.deepcopy(poschodia), kde_je_vytah+1, [vc], kolo+1, True)

            if pocet_veci > 1:
                for i in range(pocet_veci):
                    for j in range(pocet_veci):
                        if i != j:
                            moznost = [poschodia[kde_je_vytah][i], poschodia[kde_je_vytah][j]]
                            sprav_kolo(copy.deepcopy(poschodia), kde_je_vytah-1, moznost, kolo+1)
                            sprav_kolo(copy.deepcopy(poschodia), kde_je_vytah+1, moznost, kolo+1, True)


            

sprav_kolo(poschodia, kde_je_vytah)
print(min(vysledky))
