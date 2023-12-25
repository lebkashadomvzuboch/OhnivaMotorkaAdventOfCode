vysledok = 0
with open("aoc/input.txt") as subor:
    for riadok in subor.readlines():
        suradnice = set((0, 0))
        santa = [0, 0]
        robot_santa = [0, 0]
        ide_santa = True
        for zobacik in riadok.strip():
            aktualna_suradnica = santa if ide_santa else robot_santa
            if zobacik == ">":
                aktualna_suradnica[0] += 1
            elif zobacik == "<":
                aktualna_suradnica[0] -= 1
            elif zobacik == "v":
                aktualna_suradnica[1] += 1
            else:
                aktualna_suradnica[1] -= 1
            
            if ide_santa:
                santa = aktualna_suradnica
            else:
                robot_santa = aktualna_suradnica
            ide_santa = not ide_santa
                
            if not tuple(aktualna_suradnica) in suradnice:
                suradnice.add(tuple(aktualna_suradnica))
                vysledok += 1
                
        print(vysledok)
