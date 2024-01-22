vysledok = 0
odpovede = []

with open("aoc/input.txt", "r") as subor:
    l = []
    for riadok in subor.readlines():
        if riadok != "\n":
            l = l + [i for i in riadok.strip()]
        
        else:
            odpovede.append(l)
            l = []
            
    odpovede.append(l)
            
for l in odpovede:
    vysledok += len(set(l))
    
print(vysledok)

# vysledok je 6291