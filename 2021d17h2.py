udaje = "target area: x=288..330, y=-96..-50"

rozsah_x, rozsah_y = [udaj.split("=")[1].split("..")
                      for udaj in udaje.strip("target area: ").split(", ")]

rozsah_x = [int(i) for i in rozsah_x]
rozsah_y = [int(i) for i in rozsah_y]


vysledok = 0

for x in range(500):

    for y in range(-250, 250):
        vyska_vo_vzduchu = 0
        sirka_vo_vzduchu = 0

        j = -1
        while True:
            j += 1
            vyska_vo_vzduchu += y - j
            if x - j > 0:
                sirka_vo_vzduchu += x - j

            if rozsah_y[0] <= vyska_vo_vzduchu <= rozsah_y[1] and rozsah_x[0] <= sirka_vo_vzduchu <= rozsah_x[1]:
                vysledok += 1
                break
            elif vyska_vo_vzduchu < rozsah_y[0] or sirka_vo_vzduchu > rozsah_x[1]:
                break

print(vysledok)

# vysledok je 3344 (prvy pokus)
