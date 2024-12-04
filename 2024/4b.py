krizovka, vysledok = [], 0

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        krizovka.append([i for i in riadok.strip()])

sirka, dlzka = len(krizovka[0]), len(krizovka)

for riadok in range(1, dlzka-1):
    for stlpec in range(1, sirka-1):
        if krizovka[riadok][stlpec] == "A":
            kontrola1 = f"{krizovka[riadok-1][stlpec-1]}{krizovka[riadok+1][stlpec+1]}"
            kontrola2 = f"{krizovka[riadok-1][stlpec+1]}{krizovka[riadok+1][stlpec-1]}"

            if set(kontrola1) == {"M", "S"} and set(kontrola2) == {"M", "S"}:
                vysledok += 1


                    
print(vysledok)
# vysledok je 1910

