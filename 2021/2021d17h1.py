udaje = "target area: x=288..330, y=-96..-50"

rozsah_x, rozsah_y = [udaj.split("=")[1].split("..")
                      for udaj in udaje.strip("target area: ").split(", ")]

rozsah_x = [int(i) for i in rozsah_x]
rozsah_y = [int(i) for i in rozsah_y]

mozna_rychlost_x = []
i = 0
while True:
    i += 1

    if rozsah_x[0] <= (i+1) / 2 * i <= rozsah_x[1]:
        mozna_rychlost_x.append(i)
    elif rozsah_x[0] <= (i+1) / 2 * i:
        break

# print(mozna_rychlost_x)

mozna_rychlost_y = []

i = 0
bolo = True
for i in range(1000):  # take skarede
    i += 1
    vyska_vo_vzduchu = (i+1) / 2 * i

    j = 0
    aktualna_vyska = vyska_vo_vzduchu
    while True:
        j += 1
        aktualna_vyska -= j

        if rozsah_y[0] <= aktualna_vyska <= rozsah_y[1]:
            mozna_rychlost_y.append(vyska_vo_vzduchu)
            break
        elif aktualna_vyska < rozsah_y[1]:
            break


print(max(mozna_rychlost_y))

# vysledok je 4560
