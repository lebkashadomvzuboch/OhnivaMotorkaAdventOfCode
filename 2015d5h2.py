vysledok = 0
with open("aoc/input.txt") as subor:
    for riadok in subor.readlines():
        p1, p2 = False, False
        riadok = riadok.strip()
        for index, znak in enumerate(riadok):
            if index > 1:
                if riadok[index] == riadok[index-2]:
                    p1 = True
                    
            if index > 0: # jak hlupak som dal elif a zytocne dlho debugoval
                if f"{riadok[index-1]}{riadok[index]}" in riadok[index+1:]:
                    p2 = True  
        
        vysledok += 1 if p1 and p2 else 0
        print(riadok, p1, p2, vysledok)

print(vysledok)