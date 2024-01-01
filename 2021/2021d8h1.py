pocet = 0

with open("aoc/input.txt", "r") as subor:
    for riadok in subor.readlines():
        dolezite = riadok.strip().split(" | ")[1].split(" ")
        for d in dolezite:
            if len(d) in (2, 4, 7, 3):
                pocet += 1
        
print(pocet)

# vysledok je 476
