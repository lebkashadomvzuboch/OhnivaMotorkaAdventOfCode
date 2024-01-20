import ast

def porovnaj(lava, prava):
    if len(lava) == 0:
        return True
    elif len(prava) == 0:
        return False


    if isinstance(lava[0], int) and isinstance(prava[0], int):
        if lava[0] < prava[0]:
            return True
        elif lava[0] > prava[0]:
            return False
        
        else:
            return porovnaj(lava[1:], prava[1:])

    elif isinstance(lava[0], list) and isinstance(prava[0], list):
        if lava[0] == prava[0]:
            return porovnaj(lava[1:], prava[1:])

        else:
            return porovnaj(lava[0], prava[0])
        
    else:
        if isinstance(lava[0], int):
            return porovnaj([lava[0]], prava[0])
        else:
            return porovnaj(lava[0], [prava[0]])
 
riadky = [[[2]], [[6]]]
with open("input.txt", "r") as subor:
    for riadok in subor.readlines():
        if riadok != "\n":
            r = riadok.strip()
            riadky.append(ast.literal_eval(r))



def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if not porovnaj(arr[j], arr[j+1]): 
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sort(riadky)
    
print((riadky.index([[6]]) + 1) * (riadky.index([[2]]) + 1))

# vysledok je 22464
