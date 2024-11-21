hrac1, hrac2 = 4, 8
vysledky = dict()

def zisti(s1, s2, ides1, v1, v2, rodicia=[]):
    if (s1, s2) in vysledky:
        if vysledky[(s1, s2)][0]:
            return vysledky[1], 0
        else:
            return 0, vysledky[1]


    rodicia.append((s1, s2))


    if s1 > 20:
        for rodic in rodicia:
            vysledky[rodic] = [True, v1]
        return 1, 0
    elif s2 > 20:
        for rodic in rodicia:
            vysledky[rodic] = [False, v2]
        return 0, 1
    
    if ides1:
        a = zisti(s1+1, s2, not ides1, 0, 0, rodicia=rodicia)
        v1, v2  = v1 + a[0], v2 + a[1]

        b = zisti(s1+2, s2, not ides1, 0, 0, rodicia=rodicia)
        v1, v2  = v1 + b[0], v2 + b[1]

        c = zisti(s1+3, s2, not ides1, 0, 0, rodicia=rodicia)
        v1, v2  = v1 + c[0], v2 + c[1]
    
    
    else:
        a = zisti(s1, s2+1, not ides1, 0, 0,rodicia=rodicia)
        v1, v2  = v1 + a[0], v2 + a[1]

        b = zisti(s1, s2+2, not ides1, 0, 0, rodicia=rodicia)
        v1, v2  = v1 + b[0], v2 + b[1]

        c = zisti(s1, s2+3, not ides1, 0, 0, rodicia=rodicia)
        v1, v2  = v1 + c[0], v2 + c[1]
    
    return v1, v2

print(zisti(hrac1, hrac2, True, 0, 0))
