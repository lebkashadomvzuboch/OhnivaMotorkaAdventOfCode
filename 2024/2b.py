riadky = []
with open("OhnivaMotorkaAdventOfCode/input.txt", "r") as subor:
    for riadok in subor.readlines():
        a = [int(i) for i in riadok.strip().split(" ")]
        if a != None:
            riadky.append(a)

vysledok = 0
for riadok in riadky:
    m, rastie, moze_byt, bola_pouzita_tolerancia = None, None, True, False
    for cislo in riadok:
        if m:
            if rastie == None:
                if cislo > m:
                    rastie = True
                elif cislo < m:
                    rastie = False
                else:
                    moze_byt = False

            else:
                if rastie and m >= cislo:
                    moze_byt = False
                elif not rastie and m <= cislo:
                    moze_byt = False

            if abs(cislo - m) > 3 or abs(cislo - m) < 1:
                moze_byt = False
        
        m = cislo

        if not bola_pouzita_tolerancia and not moze_byt:
            bola_pouzita_tolerancia = True
            moze_byt = True


    if moze_byt:
        vysledok += 1

print(vysledok)
# vysledok je 553