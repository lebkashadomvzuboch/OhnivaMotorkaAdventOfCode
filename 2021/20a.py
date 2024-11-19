riadky = None

with open("adventofcode/OhnivaMotorkaAdventOfCode/input.txt", "r") as subor:
    riadky = subor.readlines()

mapa = []
pocet_kol = 2
overovac = riadky[0].strip()

smery = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1))

def ohranic_mapu(mapa_, znak):
    dlzka_mapy = len(mapa_)
    v_m = [znak * (dlzka_mapy + 4)]*2 + [znak*2 + r + znak*2 for r in mapa_] + [znak * (dlzka_mapy + 4)]*2
    return v_m

for riadok in riadky[2:]:
    mapa.append(riadok.strip())

for kolo in range(pocet_kol):
    znak = "#" if kolo % 2 != 0 else "."
    mapa = ohranic_mapu(mapa, znak)
    sirka, vyska = len(mapa[0]), len(mapa[1])
    nova_mapa = []

    for v in range(vyska):
        nova_mapa.append("." * (sirka))

    for y in range(1, vyska-1):
        for x in range(1, sirka-1):
            kod = ""
            for smer in smery:
                kod += mapa[y+smer[0]][x+smer[1]]

            nova_mapa[y] = nova_mapa[y][:x] + overovac[int(kod.replace(".", "0").replace("#","1"), 2)] + nova_mapa[y][x+1:]

    mapa = nova_mapa
    mapa = mapa[1:-1]
    mapa = [m[1:-1] for m in mapa]

vysledok = 0
for m in mapa:
    vysledok += m.count("#")

print(vysledok)

# vysledok je 5419
