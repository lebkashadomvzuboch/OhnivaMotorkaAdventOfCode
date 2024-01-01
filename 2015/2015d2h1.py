total = 0

with open("input.txt", "r") as subor:
	for riadok in subor.readlines():
		cisla = [int(i) for i in riadok.strip().split("x")]
		m = [cisla[0]*cisla[1], cisla[0]*cisla[2], cisla[1]*cisla[2]]
		
		total += 2 * sum(m) + min(m)
		
print(total)

# vysledok je 1586300
