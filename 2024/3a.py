riadok = None
vysledok = 0

with open("input.txt", "r") as subor:
    riadok = subor.readline().strip()

for index_znaku in range(len(riadok)):
    if riadok[index_znaku:index_znaku+4] == "mul(":
        koniec = None
        for index_konca in range(index_znaku+2, len(riadok)):
            if riadok[index_konca] == ")":
                koniec = index_konca
                break

        if koniec:
            cislo1, cislo2 = None, None
            try:
                cislo1, cislo2 = [int(i) for i in riadok[index_znaku+4:index_konca].split(",")]
            except:
                pass
            
            if cislo1 and cislo2 and 0 < len(str(cislo1)) < 4 and 0 < len(str(cislo2)) < 4:
                vysledok += cislo1*cislo2

print(vysledok)
# vysledok je 159892596