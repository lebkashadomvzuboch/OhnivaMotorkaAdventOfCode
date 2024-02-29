a, b = 0, 0

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        riadok = riadok.strip()
        pismena = set(riadok)

        je_a, je_b = False, False
        for p in pismena:
            if riadok.count(p) == 2:
                je_a = True
            elif riadok.count(p) == 3:
                je_b = True

        a += 1 if je_a else 0
        b += 1 if je_b else 0 # je_b hahahhahahhaha
 
print(a * b)

# vysledok je 5390
