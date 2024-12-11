s = [int(i) for i in "0 7 198844 5687836 58 2478 25475 894".split(" ")]

for i in range(25):
    ns = []
    for kamen in range(len(s)):
        if s[kamen] == 0:
            ns.append(1)
        elif len(str(s[kamen])) % 2 == 0:
            t = str(s[kamen])
            a = int(t[:len(t)//2])
            b = int(t[len(t)//2:])
            ns.append(a)
            ns.append(b)
        else:
            ns.append(s[kamen]*2024)

    s = ns

    # print(s)

print(len(s))
# vysledok je 216996