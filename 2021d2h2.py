hlbka, vzdialenost, aim = 0, 0, 0

with open("aoc/input.txt", "r") as subor:
    for riadok in subor.readlines():
        info = riadok.strip().split(" ")
        prikaz, cislo = info[0], int(info[1])
        
        if prikaz == "forward":
            vzdialenost += cislo
            hlbka += aim * cislo
            
        else:
            aim += cislo if prikaz == "down" else -cislo
        
print(hlbka * vzdialenost)

# vysledok je 1845455714