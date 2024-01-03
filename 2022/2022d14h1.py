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
miesto_padania_piesku = [0, 500]

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

pada_piesok = True
i = 0
try:
    while pada_piesok:
        i += 1
        bod_piesku = miesto_padania_piesku
        bod_pod_pieskom = [miesto_padania_piesku[0] +
                           1, miesto_padania_piesku[1]]

        pada_jednotlive_zrniecko = True

        while pada_jednotlive_zrniecko:
            while mapa_skaly[bod_pod_pieskom[0]][bod_pod_pieskom[1]] == ".":
                bod_piesku = [bod_pod_pieskom[0], bod_pod_pieskom[1]]
                bod_pod_pieskom[0] += 1

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
        #     print(m[490:])

        # print("-------------")

except IndexError:
    print(i-1)

# vysledok je 1133
# tym errorom je to take osemetle nechce sa mi inak
