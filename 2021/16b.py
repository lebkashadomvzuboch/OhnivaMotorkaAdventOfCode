packet = "40541D900AEDC01A88002191FE2F45D1006A2FC2388D278D4653E3910020F2E2F3E24C007ECD7ABA6A200E6E8017F92C934CFA0E5290B569CE0F4BA5180213D963C00DC40010A87905A0900021B0D624C34600906725FFCF597491C6008C01B0004223342488A200F4378C9198401B87311A0C0803E600FC4887F14CC01C8AF16A2010021D1260DC7530042C012957193779F96AD9B36100907A00980021513E3943600043225C1A8EB2C3040043CC3B1802B400D3CA4B8D3292E37C30600B325A541D979606E384B524C06008E802515A638A73A226009CDA5D8026200D473851150401E8BF16E2ACDFB7DCD4F5C02897A5288D299D89CA6AA672AD5118804F592FC5BE8037000042217C64876000874728550D4C0149F29D00524ACCD2566795A0D880432BEAC79995C86483A6F3B9F6833397DEA03E401004F28CD894B9C48A34BC371CF7AA840155E002012E21260923DC4C248035299ECEB0AC4DFC0179B864865CF8802F9A005E264C25372ABAC8DEA706009F005C32B7FCF1BF91CADFF3C6FE4B3FB073005A6F93B633B12E0054A124BEE9C570004B245126F6E11E5C0199BDEDCE589275C10027E97BE7EF330F126DF3817354FFC82671BB5402510C803788DFA009CAFB14ECDFE57D8A766F0001A74F924AC99678864725F253FD134400F9B5D3004A46489A00A4BEAD8F7F1F7497C39A0020F357618C71648032BB004E4BBC4292EF1167274F1AA0078902262B0D4718229C8608A5226528F86008CFA6E802F275E2248C65F3610066274CEA9A86794E58AA5E5BDE73F34945E2008D27D2278EE30C489B3D20336D00C2F002DF480AC820287D8096F700288082C001DE1400C50035005AA2013E5400B10028C009600A74001EF2004F8400C92B172801F0F4C0139B8E19A8017D96A510A7E698800EAC9294A6E985783A400AE4A2945E9170"

packet = bin(int(packet, 16))[2:]
if not len(packet) % 8 == 0:
    packet = "0" * (8 - (len(packet) % 8)) + packet


def prehladaj_packet(packet, current_index):
    if current_index < len(packet):
        typ_id = int(packet[current_index+3:current_index+6], 2)
        current_index += 6

        if typ_id == 4:
            cislo = ""
            while True:
                if packet[current_index] == "1":
                    cislo += packet[current_index+1: current_index+5]
                    current_index += 5

                else:
                    cislo += packet[current_index+1: current_index+5]
                    current_index += 5
                    break

            return current_index, int(cislo, 2)

        else:
            cisla = []
            hodnota = None

            typ = packet[current_index]
            current_index += 1

            if typ == "0":
                dlzka_bitov = int(packet[current_index: current_index+15], 2)
                current_index += 15

                novy_packet = packet[current_index: current_index+dlzka_bitov]

                current_index += dlzka_bitov

                aha_index = 0
                while aha_index < dlzka_bitov:
                    packet_rozbaleny = prehladaj_packet(novy_packet, aha_index)
                    if packet_rozbaleny:
                        aha_index = packet_rozbaleny[0]
                        cisla.append(packet_rozbaleny[1])

                    else:
                        break

            else:
                limit_packetov = int(
                    packet[current_index: current_index+11], 2)
                current_index += 11

                for i in range(limit_packetov):
                    packet_rozbaleny = prehladaj_packet(
                        packet, current_index)
                    current_index = packet_rozbaleny[0]
                    cisla.append(packet_rozbaleny[1])

            if typ_id == 0:
                hodnota = sum(cisla)

            if typ_id == 1:
                if len(cisla) != 0:
                    a = 1
                    for c in cisla:
                        a *= c
                    hodnota = a
                else:
                    hodnota = 0

            if typ_id == 2:
                hodnota = min(cisla)

            if typ_id == 3:
                hodnota = max(cisla)

            if typ_id == 5:
                hodnota = 1 if cisla[0] > cisla[1] else 0

            if typ_id == 6:
                hodnota = 1 if cisla[0] < cisla[1] else 0

            if typ_id == 7:
                hodnota = 1 if cisla[0] == cisla[1] else 0

            return current_index, hodnota

    return 0

print(prehladaj_packet(packet, 0)[1])

# vysledok je 10637009915279
# trvalo to brutalne dlho
# take ze a < b = b > a ibaze to ma byt a < b = b >= a a take hluposti
# ale absolutne neverim ze som to dal, som sa na to chcel vykaslat ale brutalne som sa premohol
