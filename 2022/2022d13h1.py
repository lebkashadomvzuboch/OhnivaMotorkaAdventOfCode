import ast
vysledok = 0

def porovnaj(lava, prava):
    if len(lava) == 0:
        return True
    elif len(prava) == 0:
        return False


    if isinstance(lava[0], int) and isinstance(prava[0], int):
        if lava[0] < prava[0]:
            return True
        elif lava[0] > prava[0]:
            return False
        
        else:
            return porovnaj(lava[1:], prava[1:])

    elif isinstance(lava[0], list) and isinstance(prava[0], list):
        if lava[0] == prava[0]:
            return porovnaj(lava[1:], prava[1:])

        else:
            return porovnaj(lava[0], prava[0])
        
    else:
        if isinstance(lava[0], int):
            return porovnaj([lava[0]], prava[0])
        else:
            return porovnaj(lava[0], [prava[0]])
 
poradie = 0
with open("input.txt", "r") as subor:
    riadok = "s"
    while riadok != "":
        lava, prava = ast.literal_eval(subor.readline().strip()), ast.literal_eval(subor.readline().strip())
        riadok = subor.readline()
        poradie += 1

        if porovnaj(lava, prava):
            vysledok += poradie
print(vysledok)

# vysledok je 6428
# konecne
