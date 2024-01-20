opice = dict()
with open("aoc/input.txt", "r") as subor:
    while True:
        riadok = subor.readline().strip()
        if riadok != "":
            starting_items, operation, test, ak_hej, ak_nie = [subor.readline().strip("\n") for i in range(5)]
            opica_na_pridanie = dict()
            opica_na_pridanie["veci"] = [int(i) for i in starting_items.split(": ")[1].split(", ")]
            opica_na_pridanie["operacia"] = operation.split(" = ")[1].split(" ")
            opica_na_pridanie["test"] = int(test.split("by ")[1])
            opica_na_pridanie["ak hej"] = ak_hej.split("monkey ")[1]
            opica_na_pridanie["ak nie"] = ak_nie.split("monkey ")[1]
            opica_na_pridanie["pocet_hodeni"] = 0
            
            
            subor.readline()
            opice[riadok.strip(":").split(" ")[1]] = opica_na_pridanie
            
        else:
            break

for i in range(20):
    for opica in opice:
        for item in opice[opica]["veci"]:
            c1, op, c2 = item if opice[opica]["operacia"][0] == "old" else int(opice[opica]["operacia"][0]), opice[opica]["operacia"][1], item if opice[opica]["operacia"][2] == "old" else int(opice[opica]["operacia"][2])
            nove_cislo = None
            if op == "+":
                nove_cislo = c1 + c2
            elif op == "*":
                nove_cislo = c1 * c2
                
            nove_cislo  = nove_cislo // 3
                
            if nove_cislo % int(opice[opica]["test"]) == 0:
                opice[opice[opica]["ak hej"]]["veci"].append(nove_cislo)
            else:
                opice[opice[opica]["ak nie"]]["veci"].append(nove_cislo)
                
            opice[opica]["pocet_hodeni"] += 1
            opice[opica]["veci"] = []
            
hodenia = []

for opica in opice:
    hodenia.append(opice[opica]["pocet_hodeni"])
    
hodenia.sort(reverse=True)
print(hodenia[0]*hodenia[1])

# vyskedok je 58786
