h1, h2 = 5, 8
h1s, h2s = 0, 0
ide_h1 = False
kocka = 0
riesenie = {0}

while h1s < 1000 and h2s < 1000:
    ide_h1 = not ide_h1
    v = 0

    for i in range(3):
        kocka += 1
        v += kocka

    if ide_h1:
        if (h1 + v) % 10 == 0:
            h1 = 10
            h1s += h1

        else:
            h1 = (h1 + v) % 10
            h1s += h1
    else:
        if (h2 + v) % 10 == 0:
            h2 = 10
            h2s += h2

        else:
            h2 = (h2 + v) % 10
            h2s += h2
    
        

print(kocka, h2s, h1s)

        
