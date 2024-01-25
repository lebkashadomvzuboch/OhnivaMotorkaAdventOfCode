cisla = [[1, 2 ,3], 
         [4, 5, 6], 
         [7, 8, 9]]

vysledok = ""
pozicia = 1, 1

pohyby = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        for pokyn in riadok.strip():
            n_p = pozicia[0] + pohyby[pokyn][0], pozicia[1] + pohyby[pokyn][1]

            if 0 <= n_p[0] <= 2 and 0 <= n_p[1] <= 2:
                pozicia = n_p

        vysledok += str(cisla[pozicia[0]][pozicia[1]])

print(int(vysledok))

# vysledok je 48584
