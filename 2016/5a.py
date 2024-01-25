import hashlib
zadanie = "reyedfim"
heslo = ""

i = 0
while True:
    nove_heslo = zadanie + str(i)
    hash_novy = hashlib.md5(nove_heslo.encode('utf-8')).hexdigest()

    if hash_novy.startswith("00000"):
        heslo += hash_novy[5]

    if len(heslo) == 8:
        print(heslo)
        break

    i += 1


# vysledok je f97c354d
