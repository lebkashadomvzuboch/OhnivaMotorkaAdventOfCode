import re
molekuly = dict()
velka_molekula = None

with open("input.txt", "r") as subor:
    while True:
        riadok = subor.readline()
        if riadok == "\n":
            break
        info = riadok.strip().split(" => ")
        if info[0] in molekuly:
            molekuly[info[0]].append(info[1])
        else:
            molekuly[info[0]] = [info[1]]

    velka_molekula = subor.readline().strip()


nove_molekuly = set()

for molekula in molekuly:
    for nahradna_molekula in molekuly[molekula]:
        for index_vyskytu in [m.start() for m in re.finditer(molekula, velka_molekula)]:
            v = velka_molekula[:index_vyskytu] + nahradna_molekula + \
                velka_molekula[index_vyskytu+len(molekula):]
            nove_molekuly.add(v)

print(len(nove_molekuly))

# vysledok je 518
