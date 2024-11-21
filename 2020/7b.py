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

def rataj_tasky(taska):
    pocet = 0

    if tasky[taska]:
        for dalsia_taska in tasky[taska]:
            kolko_krat = tasky[taska][dalsia_taska]
            pocet += kolko_krat
            pocet += kolko_krat * rataj_tasky(dalsia_taska)

    return pocet

print(rataj_tasky(moja_taska))
# vysledok je 29547