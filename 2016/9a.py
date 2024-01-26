riadok = None

with open("input.txt", "r") as subor:
    riadok = subor.readline().strip()


def prehladaj(riadok, pocet_znakov=0):
    z_i_z, k_i_z = None, None
    for index in range(len(riadok)):
        if riadok[index] == "(":
            z_i_z = index

        elif riadok[index] == ")":
            k_i_z = index

        if z_i_z != None and k_i_z:
            if z_i_z < k_i_z:
                udaj = riadok[z_i_z+1:k_i_z]
                pocet_znakov_, pocet_opakovani = [
                    int(i) for i in udaj.split("x")]

                pocet_znakov += pocet_znakov_*pocet_opakovani
                pocet_znakov -= k_i_z - z_i_z + 1

                pocet_znakov += prehladaj(riadok[index+pocet_znakov_:])
                return pocet_znakov

        else:
            pocet_znakov += 1

    return pocet_znakov


print(prehladaj(riadok))
