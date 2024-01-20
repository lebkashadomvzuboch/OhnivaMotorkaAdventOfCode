pocet_darcekov = 29000000

domy = [0 for i in range(pocet_darcekov//11)]

for elf in range(1, len(domy) + 1):
    for dom in range(elf, min(len(domy), elf * 50+1), elf):
        domy[dom] += elf * 11

for index, darceky in enumerate(domy):
    if darceky >= pocet_darcekov:
        print(index)
        break

# vysledok je 705600
# kusok pomalsie ale funguje
