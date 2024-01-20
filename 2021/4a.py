bingo = []
cisla = None


with open("input_.txt", "r") as subor:
    current_board = None
    cisla = [int(i) for i in subor.readline().strip().split(",")]
    for riadok in subor.readlines():
        if riadok == "\n":
            if current_board:
                bingo.append(current_board)
            current_board = []

        else:
            current_board.append(
                [int(i) for i in riadok.strip().split(" ") if i != ""])

kriziky = [[["O" for i in range(5)] for i in range(5)]
           for i in range(len(bingo))]


def hladaj():
    for cislo in cisla:
        for cislo_binga, jednotlive_bingo in enumerate(bingo):
            for cislo_riadku, riadok in enumerate(jednotlive_bingo):
                for cislo_stlpca, cislo_v_riadku in enumerate(riadok):
                    if cislo == cislo_v_riadku:
                        kriziky[cislo_binga][cislo_riadku][cislo_stlpca] = "X"

        for cislo_krizikov in range(len(kriziky)):
            for i in range(5):
                je_v_riadku, je_v_stlpci = True, True

                for stlpec in range(5):
                    if kriziky[cislo_krizikov][i][stlpec] == "O":
                        je_v_riadku = False
                        break

                for riadok in range(5):
                    if kriziky[cislo_krizikov][riadok][i] == "O":
                        je_v_stlpci = False
                        break

                if je_v_stlpci or je_v_riadku:
                    return cislo, cislo_krizikov


vyherne_cislo, cislo_binga = hladaj()

neoznacene = 0
for index_riadku, riadok in enumerate(kriziky[cislo_binga]):
    for index_stlpca, vec in enumerate(riadok):
        if vec == "O":
            neoznacene += bingo[cislo_binga][index_riadku][index_stlpca]

print(neoznacene * vyherne_cislo)

# vysledok je 29440
