with open("input_.txt", "r") as subor:
    cisla = [int(i.strip()) for i in subor.readlines()]
    for c1 in cisla:
        for c2 in cisla[1:]:
            for c3 in cisla[2:]:
                if c1 + c2 + c3 == 2020:
                    print(c1*c2*c3)
                    quit()

# vysledok je 263819430
