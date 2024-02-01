hodnoty = {"a": 0, "b": 0, "c": 1, "d": 0}
instrukcie = []
pointer = 0
with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        instrukcie.append(riadok.strip())

max_pointer = len(instrukcie) - 1


while 0 <= pointer <= max_pointer:
    prikaz = instrukcie[pointer]

    if prikaz.startswith("cpy"):
        info = prikaz.split(" ")
        hodnoty[info[2]] = int(
            info[1]) if info[1].isnumeric() else hodnoty[info[1]]
        pointer += 1

    elif prikaz.startswith("inc"):
        info = prikaz.split(" ")
        hodnoty[info[1]] += 1
        pointer += 1

    elif prikaz.startswith("dec"):
        info = prikaz.split(" ")
        hodnoty[info[1]] -= 1
        pointer += 1

    elif prikaz.startswith("jnz"):
        info = prikaz.split(" ")
        m = True
        if info[1].isnumeric():
            if info[1] == "0":
                m = False
        elif hodnoty[info[1]] == 0:
            m = False

        if m:
            pointer += int(info[2])
        else:
            pointer += 1

print(hodnoty["a"])

# vysledok je 9227737
