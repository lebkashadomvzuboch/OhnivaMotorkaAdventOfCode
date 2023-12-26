total = 0
minule = 999

with open("aoc/input.txt", "r") as subor:
    for riadok in subor.readlines():
        riadok = int(riadok.strip())
        
        if riadok > minule:
            total += 1
            
        minule = riadok
        
print(total)

# vysledok je 1676
