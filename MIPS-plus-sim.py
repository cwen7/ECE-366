


# Remembers where each of the jump labels is, and the target location
def saveJumpLabel(asm, labelIndex, labelName):
    lineCount = 0
    for line in asm:
        line = line.replace(" ", "")
        if (line.count(":")):
            labelName.append(line[0:line.index(":")])  # append the label name
            labelIndex.append(lineCount)  # append the label's index
            asm[lineCount] = line[line.index(":") + 1:]
        lineCount += 1
    for item in range(asm.count('\n')):  # Remove all empty lines '\n'
        asm.remove('\n')

def main():
    DIC = 0
    labelIndex = []
    labelName = []
    f = open("mc.txt", "w+")
    h = open("testtcase.asm", "r")
    asm = h.readlines()
    for item in range(asm.count('\n')):  # Remove all empty lines '\n'
        asm.remove('\n')

    saveJumpLabel(asm, labelIndex, labelName)  # Save all jump's destinations

    # this block of code allocates all the memory for address ranging from 0x2000 - 0x3000 if you uncomment the commented area and run it you will see
    memory = []

    g = 0
    for i in range(1025):
        mem =hex(4096 *2 + i*4)
        memory.append(['00', '00', '00', '00', mem])
        g = g + 1
        ##print(memory[i]) if (g == 8) else print(memory[i], end=" ")
        if g == 8:
            g = 0
    # uncomenting this gives you a space to raed the out put more claerly
    ##print()

    # this block creates ann array for all the registers and at the same time it allocates space for lo hi and pc
    reg = []
    for i in range(27):  # lo == index 24 hi == index 25  PC == index 26
        reg.append('00000000')
        ##print('r', i, reg[i]) if (i < 24) else print('hi, lo or pc',i, reg[i])

    # this will make accessing lo, hi, pc easy to remember
    lo = 24  # reg[lo]    reg[8] reg[pc] reg[23]
    hi = 25  # reg[hi]
    pc = 26  # reg[pc]

    location = 0
    j = 0
    line = asm[0]
    line = ''.join(str(e) for e in line)

    while location < len(asm):
        ##if j == 8:
          ##  location = 10
            ##line = asm[location]
            ##line = ''.join(str(e) for e in line)
        
        location += 1
        line = line.replace("\n", "")  # Removes extra chars
        line = line.replace("$", "")
        line = line.replace(" ", "")
        line = line.replace("zero", "0")  # assembly can also use both $zero and $0
        print(line)
        #print(j, line)








        if (line[0:4] == "addi"):  # ADDI
            line = line.replace("addi", "")
            line = line.split(",")

            if line[2][0:2] == "0x" or line[2][0:3] == "-0x":
                line[2] = line[2].replace("0x", "")
                imm = int(line[2], 16)
            else:
                imm = int(line[2], 10)
            rs = int(line[1])
            rt = int(line[0])
            rs = int(reg[rs], 16)

            if rs > 2**31 - 1:
                rs = rs - 2**32

            if rt != 0:
                reg[rt] = rs + imm
                if reg[rt] < 0:
                    reg[rt] = reg[rt] + 2**32
                #print(reg[rt])
                reg[rt] = format(reg[rt], '08x')
            print(reg[rt], 'index', rt)
            DIC = DIC + 1
            #print(int(DIC), "DIC")

        if (line[0:3] == "add"):  # ADD
            line = line.replace("add", "")
            line = line.split(",")
            rd = int(line[0], 10)
            rs = int(line[1], 10)
            rt = int(line[2], 10)
            rs = int(reg[rs], 16)
            rt = int(reg[rt], 16)

            if rs > 2 ** 31 - 1:
                rs = rs - 2 ** 32

            if rt > 2 ** 31 - 1:
                rt = rt - 2 ** 32
            result = rt + rs
            if result < 0:
                result = result + 2**32
            if rd != 0:
                reg[rd] = format(result, '08x')
            #print(reg[rd])
            DIC = DIC + 1
            #print(int(DIC), "DIC")

        if (line[0:3] == "lui"):  # LUI
            line = line.replace("lui", "")
            line = line.split(",")
            if line[1][0:2] == "0x" or line[1][0:3] == "-0x":
                line[1] = line[1].replace("0x", "")
                imm = int(line[1], 16)
            else:
                imm = int(line[1], 10)
            rt = int(line[0])
            if rt != 0:
                reg[rt] = format(imm*(16**4), '08x')
            #print(reg[rt])

            DIC = DIC + 1
            #print(int(DIC), "DIC")

        if (line[0:3] == "ori"):  #ORI
            line = line.replace("ori", "")
            line = line.split(",")

            if line[2][0:2] == "0x" or line[2][0:3] == "-0x":
                line[2] = line[2].replace("0x", "")
                imm = int(line[2], 16)
            else:
                imm = int(line[2], 10)
            rs = int(line[1])
            rt = int(line[0])
            rs = int(reg[rs], 16)

            if rs > 2**31 - 1:
                rs = rs - 2**32

            if rt != 0:
                reg[rt] = rs ^ imm
                if reg[rt] < 0:
                    reg[rt] = reg[rt] + 2**32
                reg[rt] = format(reg[rt], '08x')
            #print(reg[rt])
            DIC = DIC + 1
            #print(int(DIC), "DIC")

        if (line[0:3] == "xor"):  # XOR
            line = line.replace("xor", "")
            line = line.split(",")
            rd = int(line[0], 10)
            rs = int(line[1], 10)
            rt = int(line[2], 10)
            rs = int(reg[rs], 16)
            rt = int(reg[rt], 16)
            ##print(reg[rs])
            if rd != 0:
                reg[rd] = format(rs ^ rt, '08x')
            # print(reg[rd], "xor")
            DIC = DIC + 1
            #print(int(DIC), "DIC")


        if (line[0:3] == "and"):    #AND
            line = line.replace("and", "")
            line = line.split(",")
            rd = int(line[0], 10)
            rs = int(line[1], 10)
            rt = int(line[2], 10)
            rs = int(reg[rs], 16)
            rt = int(reg[rt], 16)
            #print(reg[rs])
            if rd != 0:
                reg[rd] = format(rs & rt, '08x')
            #print(reg[rd])
            DIC = DIC + 1
            #print(int(DIC), "DIC")


        if (line[0:2] == "sh"): #SH
            line = line.replace("sh", "")
            line = line.replace("(", ",")
            line = line.replace(")", "")
            line = line.split(",")
            if line[1][0:2] == "0x" or line[1][0:3] == "-0x":
                line[1] = line[1].replace("0x", "")
                imm = int(line[1], 16)
            else:
                imm = int(line[1], 10)
            rt = int(line[0])
            rs = int(line[2])
            rt = int(reg[rt], 16)
            rs = int(reg[rs], 16)

            ##print(rs, imm)
            address = rs + imm - 8192
            ##print(address)
            index = address // 4
            remain = address % 4

            ##print(remain)
            if remain == 0 or remain == 2:
                ##print(format(rt, '08x'))
                byte1 = rt & 255
                rt = rt >> 8
                byte2 = rt & 255
                memory[index][remain] = format(byte2, '02x')
                memory[index][remain + 1] = format(byte1, '02x')
                ##print(memory[index])

            DIC = DIC + 1
            #print(int(DIC), "DIC")


        if (line[0:3] == "lbu"):  # LW
            line = line.replace("lbu", "")
            line = line.replace("(", ",")
            line = line.replace(")", "")
            line = line.split(",")
            if line[1][0:2] == "0x" or line[1][0:3] == "-0x":
                line[1] = line[1].replace("0x", "")
                imm = int(line[1], 16)
            else:
                imm = int(line[1], 10)
            rt = int(line[0])
            rs = int(line[2])
            rs = int(reg[rs], 16)

            ##print(rs, imm)
            address = rs + imm - 8192
            ##print(address)
            index = address // 4
            remain = address % 4
            reg[rt] = '000000' + memory[index][remain]
            ##print(reg[rt])

            DIC = DIC + 1
            #print(int(DIC), "DIC")



        if (line[0:2] == "sb"):  # SB
            line = line.replace("sb", "")
            line = line.replace("(", ",")
            line = line.replace(")", "")
            line = line.split(",")
            if line[1][0:2] == "0x" or line[1][0:3] == "-0x":
                line[1] = line[1].replace("0x", "")
                imm = int(line[1], 16)
                #reg[rt] = 'ffe3'
            else:
                imm = int(line[1], 10)
            print(line[0])
            rt = int(line[0])
            rs = int(line[2])
            rt = int(reg[rt], 16)
            rs = int(reg[rs], 16)

            ##print(rs, imm)
            address = rs + imm - 8192
            ##print(address)
            index = address // 4
            remain = address % 4

            ##print(remain)

            ##print(format(rt, '08x'))
            byte1 = rt & 255
            memory[index][remain] = format(byte1, '02x')
            ##print('what did this do')
            #print(memory[index])
            DIC = DIC + 1
            #print(int(DIC), "DIC")

        if (line[0:2] == "lb"):  # LB
            line = line.replace("lb", "")
            line = line.replace("(", ",")
            line = line.replace(")", "")
            line = line.split(",")
            if line[1][0:2] == "0x" or line[1][0:3] == "-0x":
                line[1] = line[1].replace("0x", "")
                imm = int(line[1], 16)
            else:
                imm = int(line[1], 10)
            rt = int(line[0])
            rs = int(line[2])
            rs = int(reg[rs], 16)
            #print(rs, imm)
            address = rs + imm - 8192
            #print(address)
            index = address // 4
            remain = address % 4
            mem = int(memory[index][remain], 16)

            if mem > 2 ** 7 - 1:
                reg[rt] = 'ffffff' + format(mem, '02x')
            else:
                reg[rt] = format(mem, '08x')
            #print(reg[rt])
            DIC = DIC + 1
            #print(int(DIC), "DIC")

        if (line[0:4] == "sltu"):  # SLTU
            line = line.replace("sltu", "")
            line = line.split(",")
            rd = int(line[0], 10)
            rs = int(line[1], 10)
            rt = int(line[2], 10)
            rs = int(reg[rs], 16)
            rt = int(reg[rt], 16)
            # print(reg[rs])

            if rs < rt:
                reg[rd] = '00000001'
            else:
                reg[rd] = '00000000'
            #print(reg[rd], "sltu")
            DIC = DIC + 1
            #print(int(DIC), "DIC")

        if (line[0:5] == "multu"):  # MULTU
            #print('multu')
            line = line.replace("multu", "")
            line = line.split(",")
            rs = int(line[0], 10)
            rt = int(line[1], 10)
            rs = int(reg[rs], 16)
            rt = int(reg[rt], 16)
            #print(reg[10], reg[11])

            result = rs*rt

            if result < 0:
                result = result + 2**64

            low = result & 2**32 - 1
            result = result >> 32
            high = result & 2**32 - 1
            reg[lo] = format(low, '08x')
            reg[hi] = format(high, '08x')
            #print(reg[hi], reg[lo])

            #print(reg[rt], "multu")
            DIC = DIC + 1
            #print(int(DIC), "DIC")

        if (line[0:4] == "mflo"):  # MFLO
            line = line.replace("mflo", "")
            line = line.split(",")
            rd = int(line[0], 10)

            if rd != 0:
                reg[rd] = reg[lo]
            #print(reg[rd], "mflo")
            DIC = DIC + 1
            #print(int(DIC), "DIC")

        if (line[0:4] == "mfhi"):  # MFHI
            line = line.replace("mfhi", "")
            line = line.split(",")
            rd = int(line[0], 10)

            if rd != 0:
                reg[rd] = reg[hi]
            #print(reg[rd], "mfhi")
            DIC = DIC + 1
            #print(int(DIC), "DIC")

        if line[0:3] == "beq":  # BEQ
            line = line.replace("beq", "")
            line = line.split(",")
            for i in range(len(labelName)):
                if labelName[i] == line[2]:
                    labellocation = labelIndex[i]

            offset = labellocation - location + 1
            rt = int(line[1])
            rs = int(line[0])
            rs = int(reg[rs], 16)
            rt = int(reg[rt], 16)
            if rs == rt:
                for i in range(len(labelName)):
                    if labelName[i] == line[2]:
                        labellocation = labelIndex[i]

                location = labellocation
                line = asm[location]
                line = ''.join(str(e) for e in line)

            DIC = DIC + 1
            #print(int(DIC), "DIC")


        if line[0:3] == "bne":  # BNE
            line = line.replace("bne", "")
            line = line.split(",")
            rt = int(line[1])
            rs = int(line[0])
            rs = int(reg[rs], 16)
            print(rt)
            rt = int(reg[rt], 16)

            #print(rs, rt)
            if rs != rt:
                for i in range(len(labelName)):
                    if labelName[i] == line[2]:
                        labellocation = labelIndex[i]

                location = labellocation
                line = asm[location]
                line = ''.join(str(e) for e in line)
            #print('bne')
            DIC = DIC + 1
            #print(int(DIC), "DIC")
        if location != len(asm):
            line = asm[location]
            line = ''.join(str(e) for e in line)

    f.close()

    for i in range(64):
        g = g + 1
        f.write(memory[i][4] + ' ' + memory[i][0] + memory[i][1] + memory[i][2] + memory[i][3]) if (g == 8) else print(memory[i][4] + ' ' + memory[i][0] + memory[i][1] + memory[i][2] + memory[i][3] + '\n')
        if g == 8:
            g = 0
    for i in range(27):
        if (i == 0 or 7 < i < 24):
            f.write(' $' + reg[i] + '\n')
        if (i == 25 ):
            f.write('lo' + reg[i] + '\n')
        if (i == 25):
            f.write('hi' + reg[i] + '\n')
        if (i == 25 ):
            f.write('pc' + reg[i] + '\n')
if __name__ == "__main__":
    main()
