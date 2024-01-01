import functools

informacie = dict()


with open("input_.txt", "r") as subor:
    for riadok in subor.readlines():
        a, b = riadok.strip().split(" -> ")

        informacie[b] = a


@functools.cache
def spracuj_signal(pismeno):
    a = informacie[pismeno]
    if informacie[pismeno].isnumeric():
        return int(informacie[pismeno])

    elif " " not in informacie[pismeno]:
        return spracuj_signal(informacie[pismeno])

    elif informacie[pismeno].startswith("NOT"):
        nove_pismeno = informacie[pismeno].split(" ")[1]
        return 65535 - spracuj_signal(nove_pismeno)

    elif "SHIFT" in informacie[pismeno]:
        pismeno1, operacia, pismeno2 = informacie[pismeno].split(" ")
        pismeno1 = spracuj_signal(pismeno1)
        pismeno2 = int(pismeno2)

        if operacia == "LSHIFT":
            return pismeno1 << pismeno2
        elif operacia == "RSHIFT":
            return pismeno1 >> pismeno2

    else:
        pismeno1, operacia, pismeno2 = informacie[pismeno].split(" ")
        if not pismeno1.isnumeric():
            pismeno1 = spracuj_signal(pismeno1)
        else:
            pismeno1 = int(pismeno1)

        if not pismeno2.isnumeric():
            pismeno2 = spracuj_signal(pismeno2)
        else:
            pismeno2 = int(pismeno2)

        if operacia == "AND":
            return pismeno1 & pismeno2
        elif operacia == "OR":
            return pismeno1 | pismeno2


print(spracuj_signal("a"))

# vysledok je 3176
