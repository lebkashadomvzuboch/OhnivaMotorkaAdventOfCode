from functools import cache
aktualny_priecinok = None
priecinky = {}
total = 0


@cache
def prehladaj_priecinok(priecinok):
    total = 0
    for vec in priecinky[priecinok]:
        if isinstance(vec, int):
            total += vec
        else:
            total += prehladaj_priecinok(vec)

    return total


with open("input_.txt") as subor:
    for riadok in subor.readlines():
        if riadok.startswith("$ cd "):
            kam = riadok[5:].strip()
            if aktualny_priecinok:
                if kam == "..":
                    aktualny_priecinok = aktualny_priecinok[0:aktualny_priecinok.rfind(
                        "/")]
                else:
                    aktualny_priecinok += "/" + kam
            else:
                aktualny_priecinok = kam

        else:
            if not riadok.startswith("$"):
                if not aktualny_priecinok in priecinky:
                    priecinky[aktualny_priecinok] = []

                if riadok.startswith("dir "):
                    priecinky[aktualny_priecinok].append(
                        aktualny_priecinok + "/" + riadok.strip().split("dir ")[1])
                else:
                    priecinky[aktualny_priecinok].append(
                        int(riadok.strip().split(" ")[0]))

for priecinok in priecinky:
    v = prehladaj_priecinok(priecinok)

    total += v if v <= 100000 else 0

print(total)
# vysledok je 1582412
