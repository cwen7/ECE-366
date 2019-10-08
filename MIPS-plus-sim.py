


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
        print('r', i, reg[i]) if (i < 24) else print('hi, lo or pc',i, reg[i])

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
                rs = reg[rs] - 2**32

            reg[rt] = rs + imm

            if reg[rt] < 0:
                reg[rt] = reg[rt] + 2**32
            if rt != 0:
                print(reg[rt])
                reg[rt] = format(reg[rt], '08x')
            print(reg[rt])

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
            print(reg[rt])

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
            if rs > 2**31:
                rs = rs - 2**32
            if rt != 0:
                reg[rt] = rs ^ imm
            if reg[rt] < 0:
                reg[rt] = reg[rt] + 2**32
            reg[rt] = format(reg[rt], '08x')
            print(reg[rt])

        if (line[0:3] == "xor"):   # XOR
            print(' xor not ready')

        if (line[0:3] == "and"):    #AND
            line = line.replace("and", "")
            line = line.split(",")
            rd = int(line[0], 10)
            rs = int(line[1], 10)
            rt = int(line[2], 10)
            reg[rs] = int(reg[rs], 16)
            reg[rt] = int(reg[rt], 16)
            if rd != 0:
                reg[rd] = format(reg[rs] & reg[rt], '08x')
            print(reg[rd])

        if (line[0:3] == "add"):  #ADD
            print('add not ready')

        if (line[0:4] == "andi"):  #ANDI

            print('andi not ready')

        if (line[0:3] == "beq"):  # BEQ
            line = line.replace("beq", "")
            line = line.split(",")
            for i in range(len(labelName)):
                if (labelName[i] == line[2]):
                    labellocation = labelIndex[i]

            ofset = labellocation - location + 1
            imm = format(ofset, '016b') if (ofset > 0) else format(65536 + ofset, '016b')
            rt = format(int(line[1]), '05b')
            rs = format(int(line[0]), '05b')
            f.write(str('000100') + str(rs) + str(rt) + str(imm) + '\n')

        if (line[0:3] == "bne"):  # BNE
            line = line.replace("bne", "")
            line = line.split(",")
            for i in range(len(labelName)):
                if (labelName[i] == line[2]):
                    labellocation = labelIndex[i]

            ofset = labellocation - location + 1
            imm = format(ofset, '016b') if (ofset > 0) else format(65536 + ofset, '016b')
            rt = format(int(line[1]), '05b')
            rs = format(int(line[0]), '05b')
            f.write(str('000101') + str(rs) + str(rt) + str(imm) + '\n')

        if (line[0:4] == "sltu"):  # SLTU
            line = line.replace("sltu", "")
            line = line.split(",")
            rd = format(int(line[2]), '05b')
            rt = format(int(line[1]), '05b')
            rs = format(int(line[0]), '05b')
            f.write(str('000000') + str(rs) + str(rt) + str(rd) + str('00000101011') + '\n')


        if (line[0:2] == "sh"): #SH
            line = line.replace("sh", "")
            line = line.replace("(", ",")
            line = line.replace(")", "")
            line = line.split(",")
            line2 = int(line[1]) if(int(line[1]) > 0) else (int(line[1])*-1)^65534 + 1
            imm = format(line2, '016b')
            rt = format(int(line[2]), '05b')
            rs = format(int(line[0]), '05b')
            f.write(str('101011') + str(rs) + str(rt) + str(imm) + '\n')


        if (line[0:3] == "lbu"):  # LW
            line = line.replace("lbu", "")
            line = line.replace("(", ",")
            line = line.replace(")", "")
            line = line.split(",")
            line2 = int(line[1]) if(int(line[1]) > 0) else (int(line[1])*-1)^65534 + 1
            imm = format(line2, '016b')
            rt = format(int(line[2]), '05b')
            rs = format(int(line[0]), '05b')
            f.write(str('100011') + str(rs) + str(rt) + str(imm) + '\n')

        if (line[0:2] == "sb"):  # SB
            line = line.replace("sb", "")
            line = line.replace("(", ",")
            line = line.replace(")", "")
            line = line.split(",")
            line2 = int(line[1]) if(int(line[1]) > 0) else (int(line[1])*-1)^65534 + 1
            imm = format(line2, '016b')
            rt = format(int(line[2]), '05b')
            rs = format(int(line[0]), '05b')
            f.write(str('101000') + str(rs) + str(rt) + str(imm) + '\n')

        if (line[0:2] == "lb"):  # LB
            line = line.replace("lb", "")
            line = line.replace("(", ",")
            line = line.replace(")", "")
            line = line.split(",")
            line2 = int(line[1]) if(int(line[1]) > 0) else (int(line[1])*-1)^65534 + 1
            imm = format(line2, '016b')
            rt = format(int(line[2]), '05b')
            rs = format(int(line[0]), '05b')
            f.write(str('100000') + str(rs) + str(rt) + str(imm) + '\n')

        if (line[0:3] == "srl"):  # SRL
            line = line.replace("srl", "")
            line = line.split(",")
            sh = format(int(line[2]), '05b')
            rt = format(int(line[1]), '05b')
            rd = format(int(line[0]), '05b')
            f.write(str('00000000000') + str(rt) + str(rd) + str(sh) + str('000010') + '\n')

        if (line[0:5] == "multu"):  # MULTU
            line = line.replace("multu", "")
            line = line.split(",")
            rs = format(int(line[1]), '05b')
            rt = format(int(line[0]), '05b')
            f.write(str('000000') + str(rs) + str(rt) + str('0000000000011001') + '\n')












        if location != len(asm):
            line = asm[location]
            line = ''.join(str(e) for e in line)
        j += 1

    f.close()


if __name__ == "__main__":
    main()
