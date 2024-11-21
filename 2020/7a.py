riadky = None
tasky = dict()

with open("adventofcode/OhnivaMotorkaAdventOfCode/input.txt", "r") as subor:
    riadky = subor.readlines()

for riadok in riadky:
    info = riadok.strip(".\n").split("bags contain ")
    meno = info[0].strip()

    if "no " in info[1]:
        tasky[meno] = None

    else:
        veci = dict()
        for vec in info[1].split(", "):
            druhe_info = vec.split(" ")
            cislo, male_meno = int(druhe_info[0]), f"{druhe_info[1]} {druhe_info[2]}"

            veci[male_meno] = cislo

        tasky[meno] = veci

print(tasky)

moja_taska = "shiny gold"
pocet_tasiek_kde_je_moja = 0

def hladaj_tasky(taska, uz_som_pozrel=[]):
    if taska == moja_taska:
        return True
    elif tasky[taska]:
        for dalsia_taska in tasky[taska]:
            if dalsia_taska not in uz_som_pozrel:
                if hladaj_tasky(dalsia_taska, uz_som_pozrel=uz_som_pozrel+[taska]):
                    return True


for taska in tasky:
    if hladaj_tasky(taska):
        pocet_tasiek_kde_je_moja += 1

print(pocet_tasiek_kde_je_moja-1)
# vysledok je 370