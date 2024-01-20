import re
molekuly = dict()
velka_molekula = None

with open("input.txt", "r") as subor:
    while True:
        riadok = subor.readline()
        if riadok == "\n":
            break
        info = riadok.strip().split(" => ")
        if info[1] in molekuly:
            molekuly[info[1]].append(info[0])
        else:
            molekuly[info[1]] = [info[0]]

    velka_molekula = subor.readline().strip()

aktualna_molekula = "e"

vysledky = set()
prehladane = set()


def hladaj_na_jednej_urvoni(aktualna_molekula, molekuly, kroky=0):

    if aktualna_molekula == "e":
        return kroky

    else:
        for molekula in molekuly:
            if molekula in aktualna_molekula:
                for molekula_na_zmenenie in molekuly[molekula]:
                    for index_vyskytu in [m.start() for m in re.finditer(molekula, aktualna_molekula)]:

                        v = aktualna_molekula[:index_vyskytu] + molekula_na_zmenenie + \
                            aktualna_molekula[index_vyskytu +
                                              len(molekula):]

                        q = hladaj_na_jednej_urvoni(v, molekuly, kroky+1)

                        if q != None:
                            return q


print(hladaj_na_jednej_urvoni(velka_molekula, molekuly))

# vysledok je 200
# ako tak pozeram na reddit tak som na to prisiel o dost jednoduchsie ako ostatny
