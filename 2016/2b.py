cisla = [[None, None, 1, None, None],
         [None, 2 ,3, 4, None], 
         [5, 6, 7, 8, 9], 
         [None, "A", "B", "C", None],
         [None, None, "D", None, None]]

pozicie = {(0, 2), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (4, 2)}

vysledok = ""
pozicia = 2, 0

pohyby = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        for pokyn in riadok.strip():
            n_p = pozicia[0] + pohyby[pokyn][0], pozicia[1] + pohyby[pokyn][1]

            if n_p in pozicie:
                pozicia = n_p

        vysledok += str(cisla[pozicia[0]][pozicia[1]])

print(vysledok)

# vysledok je 563B6
# da sa aj lepsie
