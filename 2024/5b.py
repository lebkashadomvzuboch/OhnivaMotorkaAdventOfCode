import itertools, copy

pravidla = dict()
manualy = []
vysledok = 0

with open("input.txt", "r") as subor:
    b_p = False
    for riadok in subor.readlines():
        if riadok == "\n":
            b_p = True
            continue
        if b_p:
            manualy.append([int(i) for i in riadok.strip().split(",")])
        else:
            i = [int(i) for i in riadok.strip().split("|")]
            if i[1] in pravidla:
                pravidla[i[1]].append(i[0])
            else:
                pravidla[i[1]] = [i[0]]
                

def skontroluj_manual(manual):
    m = True
    for index_cisla, cislo in enumerate(manual):
        if cislo in pravidla:
            for pravidlo in pravidla[cislo]:
                if pravidlo in manual[index_cisla:]:
                    m = False

    return m



for manual in manualy:
    if not skontroluj_manual(manual):
        for cislo in manual:
            if cislo in pravidla:
                v = 0
                # spocitanie
                for kontrola in pravidla[cislo]:
                    if kontrola in manual:
                        v+=1

                if v == (len(manual)-1)//2:
                    vysledok += cislo
                    break


print(vysledok)
# vysledok je 4679