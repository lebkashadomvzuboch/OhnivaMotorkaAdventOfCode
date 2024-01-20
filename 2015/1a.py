total = 0
with open("input.txt", "r") as subor:
	for riadok in subor.readlines():
		for zatvorka in riadok:
			total += 1 if zatvorka == "(" else -1
			
print(total)

# vysledok je 280
			
