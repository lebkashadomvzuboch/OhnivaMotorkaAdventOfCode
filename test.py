hrac_1, hrac_2, ide_hrac_1 = 4, 8, True

def spravkolo(hrac1, hrac2, ide_hrac_1):

    if ide_hrac_1:
        spravkolo(hrac1+1, hrac2, not ide_hrac_1)
        spravkolo(hrac1+2, hrac2, not ide_hrac_1)
        spravkolo(hrac1+3, hrac2, not ide_hrac_1)
    else:
        spravkolo(hrac1, hrac2+1, not ide_hrac_1)
        spravkolo(hrac1, hrac2+2, not ide_hrac_1)
        spravkolo(hrac1, hrac2+3, not ide_hrac_1) 

    