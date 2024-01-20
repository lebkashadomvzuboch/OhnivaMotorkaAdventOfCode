with open("input_.txt", "r") as subor:
    cisla = [int(i.strip()) for i in subor.readlines()]
    for c1 in cisla:
        for c2 in cisla[1:]:
            if c1 + c2 == 2020:
                print(c1*c2)
                quit()

# vysledok je 858496
