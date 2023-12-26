udaje = []
gama = None
epsylon = None

with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        udaje.append(riadok.strip())

pocet_cislic = len(udaje[0])
udaje_2 = udaje.copy()

for index_cislice in range(pocet_cislic):
    pocet_cislic = len(udaje)
    total = 0

    for cislo in udaje:
        if cislo[index_cislice] == "1":
            total += 1

    castejsie = "1" if 2 * total >= pocet_cislic else "0"

    nove_udaje = []

    for cislo in udaje:
        if cislo[index_cislice] == castejsie:
            nove_udaje.append(cislo)

    udaje = nove_udaje

    if len(udaje) == 1:
        gama = udaje[0]
        break


pocet_cislic = len(udaje_2[0])


for index_cislice in range(pocet_cislic):
    pocet_cislic = len(udaje_2)
    total = 0

    for cislo in udaje_2:
        if cislo[index_cislice] == "1":
            total += 1

    castejsie = "0" if 2 * total >= pocet_cislic else "1"

    nove_udaje = []

    for cislo in udaje_2:
        if cislo[index_cislice] == castejsie:
            nove_udaje.append(cislo)

    udaje_2 = nove_udaje

    if len(udaje_2) == 1:
        epsylon = udaje_2[0]
        break

print(int(gama, 2) * int(epsylon, 2))

# vysledok je 2990784
# nie je to moc elegantne riesenie :(
