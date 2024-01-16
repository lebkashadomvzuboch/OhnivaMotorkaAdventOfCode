import itertools
limit = 100
ingrediencie = dict()
vysledok = 0

with open("aoc/input.txt", "r") as subor:
    for riadok in subor.readlines():
        info = riadok.strip().split(": ")
        meno = info[0]
        udaje = [int(udaj.split(" ")[1]) for udaj in info[1].split(", ")]
        
        ingrediencie[meno] = udaje
        
        
kolaciky = set(itertools.combinations_with_replacement(ingrediencie, limit))

def vynasob(vl):
    t = 1
    for v in vl:
        if v > 0:
            t *= v
        else:
            return 0
        
    return t

for kolacik in kolaciky:
    vlastnosti = [0, 0, 0, 0]
    
    for ingrediencia in kolacik:
        for i in range(4):
            vlastnosti[i] += ingrediencie[ingrediencia][i]
            
    vysledok = max(vysledok, vynasob(vlastnosti))
    
print(vysledok)
            
# vysledok je 18965440
            