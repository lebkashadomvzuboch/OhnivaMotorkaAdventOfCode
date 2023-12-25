vysledok = 0
with open("aoc/input.txt") as subor:
    for riadok in subor.readlines():
        suradnice = set((0, 0))
        aktualna_suradnica = [0, 0]
        for zobacik in riadok.strip():
            if zobacik == ">":
                aktualna_suradnica[0] += 1
            elif zobacik == "<":
                aktualna_suradnica[0] -= 1
            elif zobacik == "v":
                aktualna_suradnica[1] += 1
            else:
                aktualna_suradnica[1] -= 1
                
            if not tuple(aktualna_suradnica) in suradnice:
                suradnice.add(tuple(aktualna_suradnica))
                vysledok += 1
                
        print(vysledok)