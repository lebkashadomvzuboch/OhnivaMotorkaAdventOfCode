vysledok = 0
abeceda = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("input_.txt", "r") as subor:
    riadky = [riadok.strip() for riadok in subor.readlines()]

    for i in range(0, len(riadky), 3):
        for pismeno in set(riadky[i]):
            if pismeno in set(riadky[i+1]) and pismeno in set(riadky[i+2]):
                vysledok += abeceda.index(pismeno)
                break

print(vysledok)

# vysledok je 2641
