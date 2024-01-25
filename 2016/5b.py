import hashlib
zadanie = "reyedfim"
heslo = ["" for i in range(8)]

i = 0
while True:
    nove_heslo = zadanie + str(i)
    hash_novy = hashlib.md5(nove_heslo.encode('utf-8')).hexdigest()

    if hash_novy.startswith("00000"):
        if hash_novy[5] in {"0", "1", "2", "3", "4", "5", "6", "7"}:
            pozicia = int(hash_novy[5])
            if heslo[pozicia] == "":
                heslo[pozicia] = hash_novy[6]

    if "" not in heslo:
        print("".join(heslo))
        break

    i += 1


# vysledok je 863dde27
