parovanie = dict()
molekula = None

with open("input_.txt", "r") as subor:
    molekula = subor.readline().strip()
    subor.readline()
    for riadok in subor.readlines():
        info = riadok.strip().split(" -> ")
        parovanie[info[0]] = info[1]

pocty = dict()

for m in molekula:
    if m in pocty:
        pocty[m] += 1
    else:
        pocty[m] = 1

for i in range(10):
    nova_molekula = ""
    for index_molekuly in range(1, len(molekula)):
        par = f"{molekula[index_molekuly-1]}{molekula[index_molekuly]}"
        if par in parovanie:
            nova_molekula += par[0] + parovanie[par]

            if parovanie[par] in pocty:
                pocty[parovanie[par]] += 1
            else:
                pocty[parovanie[par]] = 1

    molekula = nova_molekula + molekula[-1]


najmensie, najvacsie = 10000000000000, 0

for cislo in pocty:
    najmensie = min(pocty[cislo], najmensie)
    najvacsie = max(pocty[cislo], najvacsie)

print(najvacsie - najmensie)

# vysledok je 2947
