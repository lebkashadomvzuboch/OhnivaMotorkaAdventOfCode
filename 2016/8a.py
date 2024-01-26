sirka, vyska = 50, 6
displej = [["." for i in range(sirka)] for i in range(vyska)]
instrukcie = []

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        instrukcie.append(riadok.strip())

for instrukcia in instrukcie:
    if instrukcia.startswith("rect"):
        sirka_stvorca, vyska_stvorca = [
            int(i) for i in instrukcia.strip("rect ").split("x")]
        for riadok in range(vyska_stvorca):
            for stlpec in range(sirka_stvorca):
                displej[riadok][stlpec] = "#"

    elif "row" in instrukcia:
        riadok, o_kolko = [int(i) for i in instrukcia.strip(
            "rotate row y=").split(" by ")]

        n_r = ["." for i in range(sirka)]
        for stlpec in range(sirka):
            if displej[riadok][stlpec] == "#":
                n_r[(stlpec + o_kolko) % sirka] = "#"

        displej[riadok] = n_r

    elif "column" in instrukcia:
        stlpec, o_kolko = [int(i) for i in instrukcia.strip(
            "rotate column x=").split(" by ")]

        n_s = ["." for i in range(vyska)]

        for riadok in range(vyska):
            if displej[riadok][stlpec] == "#":
                n_s[(riadok + o_kolko) % vyska] = "#"

        for i in range(vyska):
            displej[i][stlpec] = n_s[i]

vysledok = 0
for d in displej:
    for p in d:
        if p == "#":
            vysledok += 1

print(vysledok)

# vysledok je 115
