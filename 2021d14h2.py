parovanie = dict()
polimery = dict()

with open("input_.txt", "r") as subor:
    molekula = subor.readline().strip()
    for i in range(1, len(molekula)):
        par = f"{molekula[i-1]}{molekula[i]}"

        if par in polimery:
            polimery[par] += 1
        else:
            polimery[par] = 1

    subor.readline()
    for riadok in subor.readlines():
        info = riadok.strip().split(" -> ")
        parovanie[info[0]] = info[1]


for i in range(40):
    nove_polimery = {}
    for polymer in polimery:
        if polymer in parovanie:
            n_p1 = f"{polymer[0]}{parovanie[polymer]}"
            n_p2 = f"{parovanie[polymer]}{polymer[1]}"

            if n_p1 in nove_polimery:
                nove_polimery[n_p1] += polimery[polymer]
            else:
                nove_polimery[n_p1] = polimery[polymer]

            if n_p2 in nove_polimery:
                nove_polimery[n_p2] += polimery[polymer]
            else:
                nove_polimery[n_p2] = polimery[polymer]

        else:
            print("aha")

    polimery = nove_polimery

pocty = dict()

najmensie, najvacsie = 10000000000000, 0


for par in polimery:
    if par[0] in pocty:
        pocty[par[0]] += polimery[par]
    else:
        pocty[par[0]] = polimery[par]

for cislo in pocty:
    najmensie = min(pocty[cislo], najmensie)
    najvacsie = max(pocty[cislo], najvacsie)

print(najvacsie - najmensie - 1)

# vysledok je 3232426226464
# neratlalo to s poclednym cislom cize som najprv tipol 3232426226465, 3232426226466, 3232426226464
# we ball
