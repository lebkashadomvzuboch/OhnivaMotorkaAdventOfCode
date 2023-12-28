jaskyne = dict()
zaciatok, koniec = "start", "end"
pocet_ciest = 0

with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        od, do = riadok.strip().split("-")

        if od in jaskyne:
            jaskyne[od].append(do)

        else:
            jaskyne[od] = [do]

        if od != zaciatok:
            if do in jaskyne:
                jaskyne[do].append(od)

            else:
                jaskyne[do] = [od]

uz_bolo = []


def dfs_hladac(jaskyna, cesta=[]):
    global pocet_ciest
    cesta = cesta + [jaskyna]

    if jaskyna == koniec:
        pocet_ciest += 1
        return

    for druha_cesta in jaskyne[jaskyna]:
        if druha_cesta.islower() and druha_cesta in cesta:
            pass

        else:
            dfs_hladac(druha_cesta, cesta)


dfs_hladac(zaciatok)
print(pocet_ciest)

# vysledok je 3463
