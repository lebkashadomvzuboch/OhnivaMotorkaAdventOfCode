total = 0

with open("input.txt", "r") as subor:
	for riadok in subor.readlines():
		cisla = [int(i) for i in riadok.strip().split("x")]
		cisla.sort()
		
		total += 2 * (cisla[0] + cisla[1]) + (cisla[0] * cisla[1] * cisla[2])
		
print(total)