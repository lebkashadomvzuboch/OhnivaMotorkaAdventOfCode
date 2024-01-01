bity = None
pocet_riadkov = 0

with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        pocet_riadkov += 1
        if not bity:
            bity = [int(i) for i in riadok.strip()]

        for index, bit in enumerate(riadok.strip()):
            bity[index] += int(bit)


gama = ""
epsylon = ""

for bit in bity:
    if bit * 2 > pocet_riadkov:
        gama += "1"
        epsylon += "0"
    else:
        gama += "0"
        epsylon += "1"

print(int(gama, 2) * int(epsylon, 2))

# vysledok je 3813416
