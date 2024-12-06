# import sys
# sys.setrecursionlimit(10000)

hrac1, hrac2 = 4, 8
vysledky = dict()

def zisti(s1, s2, ides1):
    v1, v2 = 0, 0

    if (s1, s2, ides1) in vysledky:
        return vysledky[(s1, s2, ides1)]

    if s1 > 20:
        # vysledky[(s1, s2, ides1)] = 1, 0
        return 1, 0
    elif s2 > 20:
        # vysledky[(s1, s2, ides1)] = 0, 1
        return 0, 1

    if ides1:
        va = zisti(s1+1, s2, not ides1)
        vb = zisti(s1+2, s2, not ides1)
        vc = zisti(s1+3, s2, not ides1)

        v1 += va[0] + vb[0] + vc[0]
        v2 += va[1] + vb[1] + vc[1]

    else:
        va = zisti(s1, s2 + 1, not ides1)
        vb = zisti(s1, s2 + 2, not ides1)
        vc = zisti(s1, s2 + 3, not ides1)

        v1 += va[0] + vb[0] + vc[0]
        v2 += va[1] + vb[1] + vc[1]

    vysledky[(s1, s2, ides1)] = v1, v2
    return v1, v2




print(zisti(hrac1, hrac2, True))
print(vysledky)