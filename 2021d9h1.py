morske_dno = []
smery = ((1, 0), (0, 1), (-1, 0), (0, -1))
total = 0

with open('input_.txt', "r") as subor:
    for riadok in subor.readlines():
        morske_dno.append([int(i) for i in riadok.strip()])

pocet_riadkov, pocet_stlpcov = len(morske_dno), len(morske_dno[0])

for riadok in range(pocet_riadkov):
    for stlpec, cislo in enumerate(morske_dno[riadok]):
        je_najnizsie = True

        for smer in smery:
            if 0 <= riadok + smer[0] < pocet_riadkov and 0 <= stlpec + smer[1] < pocet_stlpcov:
                if morske_dno[riadok+smer[0]][stlpec+smer[1]] <= cislo:
                    je_najnizsie = False

        if je_najnizsie:
            total += cislo + 1

print(total)

# vysledok je 522
