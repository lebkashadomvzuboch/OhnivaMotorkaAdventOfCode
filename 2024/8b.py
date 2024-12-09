riadky = []

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        riadky.append([i for i in riadok.strip()])

majaky = dict()
y_, x_ = len(riadky), len(riadky[0])

for y in range(y_):
    for x in range(x_):
        vec = riadky[y][x]
        if vec != ".":
            if vec in majaky:
                majaky[vec].append((y, x))
            else:
                majaky[vec] = [(y, x)]

prazdne_pole = [[None for i in range(x_)] for j in range(y_)]

for vec in majaky:
    b = set()
    for majak_jedna in majaky[vec]:
        for majak_dva in majaky[vec]:
            if majak_jedna != majak_dva and (majak_jedna, majak_dva) not in b:
                b.add((majak_jedna, majak_dva))

                prazdne_pole[majak_jedna[0]][majak_jedna[1]] = "#"
                prazdne_pole[majak_dva[0]][majak_dva[1]] = "#"


                vzdialenost = (majak_jedna[0]-majak_dva[0], majak_jedna[1]-majak_dva[1])

                a_a = majak_jedna[0] + vzdialenost[0], majak_jedna[1] + vzdialenost[1]
                a_b = majak_dva[0] - vzdialenost[0], majak_dva[1] - vzdialenost[1]
                a_ac, a_bc = 1, 1

                while -1 < a_a[0] < y_ and -1 < a_a[1] < x_:
                    a_ac += 1
                    prazdne_pole[a_a[0]][a_a[1]] = "#"
                    a_a = majak_jedna[0] + vzdialenost[0]*a_ac, majak_jedna[1] + vzdialenost[1]*a_ac


                while -1 < a_b[0] < y_ and -1 < a_b[1] < x_:
                    a_bc += 1
                    prazdne_pole[a_b[0]][a_b[1]] = "#"
                    a_b = majak_dva[0] - vzdialenost[0]*a_bc, majak_dva[1] - vzdialenost[1]*a_bc


vysledok = 0
for p in prazdne_pole:
    for l in p:
        if l == "#":
            vysledok += 1

print(vysledok)# vysledok je 934