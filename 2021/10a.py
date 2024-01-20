tabulka = {")": 3, "]": 57, "}": 1197, ">": 25137}
pary = {")": "(", "]": "[", "}": "{", ">": "<"}
vysledok = 0

with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        zatvorky = []
        for zatvorka in riadok.strip():
            if zatvorka in ")]}>":
                if zatvorky[-1] != pary[zatvorka]:
                    vysledok += tabulka[zatvorka]
                    break

                else:
                    zatvorky = zatvorky[:-1]

            else:
                zatvorky.append(zatvorka)

print(vysledok)

# vysledok je 415953
