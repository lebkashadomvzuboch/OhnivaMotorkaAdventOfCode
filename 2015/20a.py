pocet_darcekov = 29000000

domy = [0 for i in range(pocet_darcekov//10)]

for elf in range(1, len(domy) + 1):
    for dom in range(elf, len(domy), elf):
        domy[dom] += elf * 10

for index, darceky in enumerate(domy):
    if darceky >= pocet_darcekov:
        print(index)
        break

# vysledok je 665280
# kusok pomalsie ale funguje
