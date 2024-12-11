s = [int(i) for i in "0 7 198844 5687836 58 2478 25475 894".split(" ")]
veci = dict()
for l in s:
    veci[l] = 1


for i in range(75):
    nove_veci = dict()

    for kamen in veci:
        if kamen == 0:
            if 1 in nove_veci:
                nove_veci[1] += veci[0]
            else:
                nove_veci[1] = veci[0]

        elif len(str(kamen)) % 2 == 0:
            t = str(kamen)
            a = int(t[:len(t)//2])
            b = int(t[len(t)//2:])

            if a in nove_veci:
                nove_veci[a] += veci[kamen]
            else:
                nove_veci[a] = veci[kamen]

            if b in nove_veci:
                nove_veci[b] += veci[kamen]
            else:
                nove_veci[b] = veci[kamen]

        else:
            t = kamen * 2024

            if t in nove_veci:
                nove_veci[t] += veci[kamen]
                
            else:
                nove_veci[t] = veci[kamen]

    veci = nove_veci

    # print(s)

v = 0
for n in veci:
    v += veci[n]
print(v)
# vysledok je 257335372288947