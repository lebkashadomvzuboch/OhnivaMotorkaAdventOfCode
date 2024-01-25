vysledok = 0
abeceda = "abcdefghijklmnopqrstuvwxyz"

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        info = riadok.split("[")
        cislo = int(info[0].split("-")[-1])

        r = info[0]
        for i in range(cislo):
            s = ""
            for pismeno in r:
                if pismeno.isalpha():
                    novy_index = (abeceda.index(pismeno) + 1) % len(abeceda)
                    s += abeceda[novy_index]
                else:
                    s += pismeno

            r = s

        if "north" in r:
            print(r)

# vysledok je northpole-object-storage-993
