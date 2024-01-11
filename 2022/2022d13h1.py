import ast
vysledok = 0
i = 1

def porovnaj_list(list1, list2):
    if (list1 == [] or list1 == None) and len(list2) != 0:
        return True
    if (list2 == [] or list2 == None) and len(list1) != 0:
        return False
    if isinstance(list1[0], int) and isinstance(list2[0], int):
        if list1[0] < list2[0]:
            return True
        elif list1[0] >list2[0]:
            return False
        else:
            return porovnaj_list(list1[1:], list2[1:])
                
    elif isinstance(list1[0], list) and isinstance(list2[0], list):
        if list1[0] != list2[0]:
            return porovnaj_list(list1[0], list2[0])
        else:
            return porovnaj_list(list1[1:], list2[1:])
                
    else:
        if isinstance(list1[0], int):
            list_1 = []
            list_1.append(list1)
            if list_1[0] != list2[0]:
                return porovnaj_list(list_1, list2)
            else:
                return True
        else:
            list_2 = []
            list_2.append(list2)
            if list_2[0] != list1[0]:
                return porovnaj_list(list1, list_2)
            else:
                return True
    

with open("aoc/input.txt", "r") as subor:
    riadok = "q"
    while riadok != "":
        list1, list2 = [subor.readline().strip() for i in range(2)]
        list1, list2 = ast.literal_eval(list1), ast.literal_eval(list2)
        
        if porovnaj_list(list1, list2):
            vysledok += i
        i += 1
        riadok = subor.readline()
        
        
print(vysledok)
        
