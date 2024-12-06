podlaha = []
strazca = [None, None]

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        podlaha.append([i for i in riadok.strip()])

vyska, sirka = len(podlaha), len(podlaha[0])
obsadene = [[None for i in range(sirka)] for j in range(vyska)]

for i in range(vyska):
    for j in range(sirka):
        if podlaha[i][j] == "^":
            strazca = [i, j]

smery = ((-1, 0), (0, 1), (1, 0), (0, -1))
aktualny_smer = 0

while True:
    ns = strazca[0] + smery[aktualny_smer][0], strazca[1] + smery[aktualny_smer][1]
    if not (-1 < ns[0] < vyska and -1 < ns[1] < sirka):
        break
    if podlaha[ns[0]][ns[1]] == "#":
        aktualny_smer = (aktualny_smer + 1) % 4
    
    else:
        obsadene[ns[0]][ns[1]] = "X"
        strazca = ns

vysledok = 0
for i in range(len(obsadene)):
    for j in range(len(obsadene[1])):
        if obsadene[i][j] == "X":
            vysledok += 1

print(vysledok)
# vysledok je 4776