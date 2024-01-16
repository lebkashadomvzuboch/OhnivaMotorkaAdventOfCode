reader = {
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1
}

with open("aoc/input.txt", "r") as subor:
    for riadok in subor.readlines():
        
        info = riadok.strip().split(", ")
        veci = info[1:]
        info2 = info[0].split(": ")
        meno_sue = info2[0]
        veci.append(": ".join(info2[1:]))
            
        potencial = True
        for vec in veci:
            meno, cislo = vec.split(": ")
            if reader[meno] != int(cislo):
                potencial = False
                break
                
        if potencial:
            print(meno_sue.split(" ")[1])
            break
            
# vysledok je 40
            
