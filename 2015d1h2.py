total = 0
with open("input.txt", "r") as subor:
	for riadok in subor.readlines():
		for index, zatvorka in enumerate(riadok):
			total += 1 if zatvorka == "(" else -1
			
			if total < 0:
				print(index + 1)
				break
			
