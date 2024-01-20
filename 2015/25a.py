row, column = 2947, 3029
start = 20151125
multiplicator, divider = 252533, 33554393


def najdi_poradie(row, column):
    o_kolko_sa_zvacsilo = ((row) * (row-1) // 2) + 1
    o_kolko_sa_zvacsilo_potom = (row+row+column) * (column-1) // 2

    return o_kolko_sa_zvacsilo + o_kolko_sa_zvacsilo_potom


poradie = najdi_poradie(row, column)

vysledok = start

for i in range(poradie-1, 10):
    vysledok *= multiplicator
    vysledok %= divider

print(vysledok)

# vysledok je 19980801
