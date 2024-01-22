vysledok = 0
odpovede = []

with open("aoc/input.txt", "r") as subor:
    l = []
    for riadok in subor.readlines():
        if riadok != "\n":
            l.append([i for i in riadok.strip()])
        
        else:
            odpovede.append(l)
            l = []
            
    odpovede.append(l)
    
for odpoved in odpovede:
    if len(odpoved) == 1:
        vysledok += len(odpoved[0])
    else:
        temp = 0
        for pismeno in odpoved[0]:
            je = True
            for druhe_odpovede in odpoved[1:]:
                if pismeno not in druhe_odpovede:
                    je = False
            
            if je:
                temp += 1
            
        vysledok += temp
    
print(vysledok)
    

# vysledok je 3052
            