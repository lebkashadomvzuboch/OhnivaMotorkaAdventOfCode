subor = None
with open("input.txt", "r") as s:
    subor = s.readline().strip()

reformatovany_subor = []
id = 0
je_volne = False

for s in subor:
    if je_volne:
        for i in range(int(s)):
            reformatovany_subor.append(".") 

    else:
        for i in range(int(s)):
            reformatovany_subor.append(id)
        id += 1

    je_volne = not je_volne

stopka = 0
dlzka_suboru = len(reformatovany_subor)

for index_od_konca in range(dlzka_suboru-1, 0, -1):
    print(index_od_konca)
    try:
        if stopka != 0:
            stopka -= 1
            continue

        # zistovanie od do
        if reformatovany_subor[index_od_konca] != ".":
            cislo = reformatovany_subor[index_od_konca]

            rozmedzie_cisla = [None, None]
            kontrola = reformatovany_subor[index_od_konca]
            rozmedzie_cisla[0] = index_od_konca

            for i in range(index_od_konca, 0, -1):
                if reformatovany_subor[i] != kontrola:
                    rozmedzie_cisla[1] = i
                    break

            bolo_cislo_zaradene = False


            # hladanie bodiek
            rozmedzie_bodiek = [None, None]
            for j in range(0, rozmedzie_cisla[1]):
                if reformatovany_subor[j] == ".":
                    rozmedzie_bodiek[0] = j
                    for k in range(j, rozmedzie_cisla[0]):
                        if reformatovany_subor[k] != ".":
                            rozmedzie_bodiek[1] = k
                            break


                # ci sa zmesti
                    if abs(rozmedzie_cisla[0]-rozmedzie_cisla[1]) <= abs(rozmedzie_bodiek[0]-rozmedzie_bodiek[1]):
                        pocet_nahradeni = abs(rozmedzie_cisla[0]-rozmedzie_cisla[1])
                        bolo_cislo_zaradene = True  

                        for t in range(rozmedzie_bodiek[0], rozmedzie_bodiek[0]+pocet_nahradeni):
                            reformatovany_subor[t] = cislo

                        for t in range(rozmedzie_cisla[1]+1, rozmedzie_cisla[0]+1):
                            reformatovany_subor[t] = "."

                        break

            if not bolo_cislo_zaradene:
                stopka = abs(rozmedzie_cisla[0]-rozmedzie_cisla[1])-1

    except TypeError:
        pass
v = 0
for i in range(len(reformatovany_subor)):
    if reformatovany_subor[i] != ".":
        v += i * int(reformatovany_subor[i])

print(v)
# vysledok je 6361380647183