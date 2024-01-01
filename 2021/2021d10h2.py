tabulka = {"(": 1, "[": 2, "{": 3, "<": 4}
pary = {")": "(", "]": "[", "}": "{", ">": "<"}
vysledok = []

with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        je_pokazena = False
        zatvorky = []
        for zatvorka in riadok.strip():
            if zatvorka in ")]}>":
                if zatvorky[-1] != pary[zatvorka]:
                    je_pokazena = True
                    break

                else:
                    zatvorky = zatvorky[:-1]

            else:
                zatvorky.append(zatvorka)

        if not je_pokazena:
            zatvorky_2 = []
            chybaju = []

            for zatvorka in riadok.strip():
                if zatvorka in ")]}>":
                    zatvorky_2.reverse()
                    zatvorky_2.remove(pary[zatvorka])
                    zatvorky_2.reverse()
                else:
                    zatvorky_2.append(zatvorka)

            if len(zatvorky_2) != 0:
                temp = 0
                zatvorky_2.reverse()
                for zatvorka_co_chyba in zatvorky_2:
                    temp *= 5
                    temp += tabulka[zatvorka_co_chyba]

                vysledok.append(temp)

vysledok.sort()
print(vysledok[round(len(vysledok) / 2)])

# vysledok je 2292863731
