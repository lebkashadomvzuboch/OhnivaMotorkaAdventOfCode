a, b, vysledok= [], [], 0

with open("OhnivaMotorkaAdventOfCode/input.txt", "r") as subor:
    for riadok in subor.readlines():
        v = [int(i.strip()) for i in riadok.split(" ") if i != ""]
        a.append(v[0])
        b.append(v[1])

a.sort()
b.sort()

for i in range(len(a)):
    vysledok += b.count(a[i]) * a[i]

print(vysledok)
# vysledok je 21607792
