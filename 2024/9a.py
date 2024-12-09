subor = None
with open("input.txt", "r") as s:
    subor = s.readline().strip()

reformatovany_subor = []
id = 0
je_volne = False

for s in subor:
    if je_volne:
        for i in range(int(s)):
            reformatovany_subor.append(".") 

    else:
        for i in range(int(s)):
            reformatovany_subor.append(id)   
        id += 1

    je_volne = not je_volne

koniec = len(reformatovany_subor)-1
for i in range(len(reformatovany_subor)):
    if reformatovany_subor[i] == ".":
        for j in range(koniec, i, -1):
            if reformatovany_subor[j] != ".":
                koniec = j
                reformatovany_subor[i], reformatovany_subor[j] = reformatovany_subor[j], reformatovany_subor[i]
                break

v = 0
for i in range(len(reformatovany_subor)):
    if reformatovany_subor[i] != ".":
        v += reformatovany_subor[i] * i

print(v)
#6337367222422

