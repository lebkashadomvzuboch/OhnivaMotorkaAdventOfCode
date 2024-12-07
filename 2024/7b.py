import itertools
riadky = []

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        riadky.append(riadok.strip())

vysledok = 0
for riadok in riadky:
    print(riadok)
    kontrola, cisla_ = riadok.split(": ")
    kontrola = int(kontrola)
    cisla = [int(i) for i in cisla_.split(" ")]
    kombinacie = list(itertools.product(("+", "*", "||"), repeat=len(cisla)-1))
    m = False

    for kombinacia in kombinacie:
        test = cisla[0]
        for i in range(len(kombinacia)):
            if kombinacia[i] == "+":
                test += cisla[i+1]
            elif kombinacia[i] == "*":
                test *= cisla[i+1]
            else:
                test = int(f"{str(test)}{cisla[i+1]}")


        if test == kontrola:
            m = True
            break


    if m:
        vysledok += kontrola

print(vysledok)
# vysledok je 20928985450275

