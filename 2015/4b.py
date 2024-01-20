import hashlib

puzzle_input_ = "iwrupvqb"

cislo = 0
while True:
    puzzle_input = f"{puzzle_input_}{cislo}"
    cislo += 1
    if hashlib.md5(puzzle_input.encode()).hexdigest().startswith("000000"):
        print(cislo-1)
        break

# vysledok je 9958218
