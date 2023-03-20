output000 = [str(int(i/100)) for i in range(0, 16*16)]
output00 = [str(int((i%100)/10)) for i in range(0, 16*16)]
output0 = [str(int(i%10)) for i in range(0, 16*16)]


number_dic = {
    "0": "77",
    "1": "41",
    "2": "3b",
    "3": "6b",
    "4": "4d",
    "5": "6e",
    "6": "7e",
    "7": "43",
    "8": "7f",
    "9": "6f",
}


if __name__ == "__main__":
    o = open("number_EEPROM_000", "w")

    o.write("v3.0 hex words addressed\n")

    for i in range (0, 16):
            o.write(str(hex(i))[-1:])
            o.write("0: ")
            for j in range (0, 15):
                o.write(number_dic[output000[i*16 + j]])
                o.write(" ")
            o.write(number_dic[output000[i*16 + 15]])
            o.write("\n")

    o.close()

    o = open("number_EEPROM_00", "w")

    o.write("v3.0 hex words addressed\n")

    for i in range (0, 16):
            o.write(str(hex(i))[-1:])
            o.write("0: ")
            for j in range (0, 15):
                o.write(number_dic[output00[i*16 + j]])
                o.write(" ")
            o.write(number_dic[output00[i*16 + 15]])
            o.write("\n")

    o.close()

    o = open("number_EEPROM_0", "w")

    o.write("v3.0 hex words addressed\n")

    for i in range (0, 16):
            o.write(str(hex(i))[-1:])
            o.write("0: ")
            for j in range (0, 15):
                o.write(number_dic[output0[i*16 + j]])
                o.write(" ")
            o.write(number_dic[output0[i*16 + 15]])
            o.write("\n")

    o.close()
    
    print("compiled successfully")


