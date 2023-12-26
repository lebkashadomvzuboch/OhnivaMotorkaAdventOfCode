hlbka, vzdialenost = 0, 0

with open("aoc/input.txt", "r") as subor:
    for riadok in subor.readlines():
        info = riadok.strip().split(" ")
        prikaz, cislo = info[0], int(info[1])
        
        if prikaz == "forward":
            vzdialenost += cislo
        else:
            hlbka -= cislo if prikaz == "up" else -cislo
        
        
        
        
print(hlbka * vzdialenost)

# vysledok je 1855814