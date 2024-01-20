total = 0
minule = [999, 999, 999]

with open("aoc/input.txt", "r") as subor:
    for riadok in subor.readlines():
        riadok = int(riadok.strip())
        
        if riadok > minule[0]:
            total += 1
            
        minule.pop(0)
        minule.append(riadok)
        
print(total)

# vysledok je 1706
