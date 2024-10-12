import math, ast
print("Fungujem")

slimacie_cisla = []
aktualne_slimacie_cislo = None

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        slimacie_cisla.append(riadok.strip())

aktualne_slimacie_cislo = slimacie_cisla[0]

def rozbi_zatvorku(bod_a, bod_b, slimacie_cislo):
    zatvorka = slimacie_cislo[bod_a+1:bod_b]
    cislo_1, cislo_2 = [int(i) for i in zatvorka.split(",")]

    polka, druha_polka = slimacie_cislo[:bod_a][::-1], slimacie_cislo[bod_b:]
    for index_znaku, znak in enumerate(polka):
        if znak.isnumeric():
            od, do = index_znaku, None

            for i, z in enumerate(polka[index_znaku:]):
                if not z.isnumeric():
                    do = index_znaku + i
                    break

            polka = polka[:od] + str(int(polka[od:do][::-1]) + cislo_1)[::-1] + polka[do:] 
            break

    for index_znaku, znak in enumerate(druha_polka):
        if znak.isnumeric():
            od, do = index_znaku, None

            for i, z in enumerate(druha_polka[index_znaku:]):
                if not z.isnumeric():
                    do = index_znaku + i
                    break

            druha_polka = druha_polka[:od] + str(int(druha_polka[od:do]) + cislo_2) + druha_polka[do:] 
            break

    return polka[::-1] + "0" + druha_polka[1:]

def skontroluj_cislo(slimacie_cislo):
    pocet_a_zatvoriek, pocet_b_zatvoriek = 0, 0

    for index_znaku, znak in enumerate(slimacie_cislo):
        if znak == "[":
            pocet_a_zatvoriek += 1
        elif znak == "]":
            pocet_b_zatvoriek += 1

        if pocet_a_zatvoriek - pocet_b_zatvoriek > 4:
            deliaci_bod_a, deliaci_bod_b = index_znaku, None
            
            for i, z in enumerate(slimacie_cislo[deliaci_bod_a:]):
                if z == "]":
                    deliaci_bod_b = deliaci_bod_a + i
                    break

            return rozbi_zatvorku(deliaci_bod_a, deliaci_bod_b, slimacie_cislo)
        
    for index_znaku, znak in enumerate(slimacie_cislo):
        if znak.isnumeric():
            od, do = index_znaku, None

            for i, z in enumerate(slimacie_cislo[index_znaku:]):
                if not z.isnumeric():
                    do = index_znaku + i
                    break

            cislo = int(slimacie_cislo[od:do])
            if cislo > 9:
                return slimacie_cislo[:od] + str([math.floor(cislo/2), math.ceil(cislo/2)]) + slimacie_cislo[do:]
        
    return slimacie_cislo

for cislo in slimacie_cisla[1:]:
    aktualne_slimacie_cislo = f"[{aktualne_slimacie_cislo}, {cislo}]"

    temp = skontroluj_cislo(aktualne_slimacie_cislo)
    while aktualne_slimacie_cislo != temp:
        aktualne_slimacie_cislo = temp
        temp = skontroluj_cislo(aktualne_slimacie_cislo)

aktualne_slimacie_cislo = ast.literal_eval(aktualne_slimacie_cislo)

def zisti_m(slimacie_cislo):
    if isinstance(slimacie_cislo, int):
        return slimacie_cislo
    
    l, p = slimacie_cislo
    return 3 * zisti_m(l) + 2 * zisti_m(p)

print(zisti_m(aktualne_slimacie_cislo))

# vyskedok je 4391
