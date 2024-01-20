ciary = []

naj_x, naj_y = 0, 0

with open('input_.txt', "r") as subor:
    for riadok in subor.readlines():
        info = riadok.strip().split(" -> ")

        ciara = []
        for par in info:
            x, y = [int(i) for i in par.split(",")]
            naj_x, naj_y = max(x, naj_x), max(y, naj_y)
            ciara.append([y, x])

        ciary.append(ciara)

mapa_skaly = [["." for i in range(naj_x+1)] for i in range(naj_y+1)]

for ciara in ciary:
    aktualny_bod = None
    for par in ciara:
        if aktualny_bod:
            if aktualny_bod[0] == par[0]:
                for i in range(min(aktualny_bod[1], par[1]), max(aktualny_bod[1], par[1])+1):
                    mapa_skaly[aktualny_bod[0]][i] = "#"
            else:
                for i in range(min(aktualny_bod[0], par[0]), max(aktualny_bod[0], par[0])+1):
                    mapa_skaly[i][aktualny_bod[1]] = "#"

        aktualny_bod = par

mapa_skaly.append(["." for i in range(naj_x+1)])
mapa_skaly.append(["#" for i in range(naj_x+1)])


i = 0
miesto_padania_piesku = [0, 500]

while mapa_skaly[miesto_padania_piesku[0]][miesto_padania_piesku[1]] == ".":
    i += 1
    bod_piesku = miesto_padania_piesku.copy()
    bod_pod_pieskom = [miesto_padania_piesku[0] +
                       1, miesto_padania_piesku[1]]

    pada_jednotlive_zrniecko = True

    while pada_jednotlive_zrniecko:
        while mapa_skaly[bod_pod_pieskom[0]][bod_pod_pieskom[1]] == ".":
            bod_piesku = [bod_pod_pieskom[0], bod_pod_pieskom[1]]
            bod_pod_pieskom[0] += 1

        if bod_pod_pieskom[1] == 0:
            for j in range(len(mapa_skaly)-1):
                mapa_skaly[j].insert(0, ".")
            miesto_padania_piesku = [
                miesto_padania_piesku[0], miesto_padania_piesku[1] + 1]

        elif bod_pod_pieskom[1] == len(mapa_skaly[0]) - 1:
            for j in range(len(mapa_skaly)-1):
                mapa_skaly[j].append(".")
            mapa_skaly[len(mapa_skaly)-1].append("#")

        if mapa_skaly[bod_pod_pieskom[0]][bod_pod_pieskom[1]-1] == ".":
            bod_piesku[1] -= 1
            bod_pod_pieskom[1] -= 1

        elif mapa_skaly[bod_pod_pieskom[0]][bod_pod_pieskom[1]+1] == ".":
            bod_piesku[1] += 1
            bod_pod_pieskom[1] += 1

        else:
            pada_jednotlive_zrniecko = False
            mapa_skaly[bod_piesku[0]][bod_piesku[1]] = "o"

    # for m in mapa_skaly:
    #     print(m[480:])

    # print(i)
    # print("-------------")

print(i)
# vysledok je 27566
# na prvy pokus
# zbytocne som 20 min debugoval lebo a = [0, 1], b = a, b[1] += 5, a[1] = 6
# som nedal b = a.copy() a vyslo ma to draho
