seats = []

with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        c1, c2 = riadok[0:7].replace("F", "0").replace(
            "B", "1"), riadok[7:].replace("L", "0").replace("R", "1")
        seats.append(8 * int(c1, 2) + int(c2, 2))

seats.sort()

for index in range(len(seats)-2):
    if seats[index+1] - seats[index] == 2:
        print(seats[index+1] - 1)
        break

# vysledok je 617
