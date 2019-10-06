


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
    h = open("testcase.asm", "r")
    asm = h.readlines()
    for item in range(asm.count('\n')):  # Remove all empty lines '\n'
        asm.remove('\n')

    saveJumpLabel(asm, labelIndex, labelName)  # Save all jump's destinations

    # this block of code allocates all the memory for address ranging from 0x2000 - 0x3000 if you uncomment the commented area and run it you will see
    memory = []

    g = 0
    for i in range(1025):
        mem =hex(4096 *2 + i*4)
        memory.append([mem, hex(00), hex(00), hex(00), hex(00)])
        g = g + 1
        ##print(memory[i]) if (g == 8) else print(memory[i], end=" ")
        if g == 8:
            g = 0
    # uncomenting this gives you a space to raed the out put more claerly
    ##print()

    # this block creates ann array for all the registers and at the same time it allocates space for lo hi and pc
    reg = [0]
    for i in range(27):  # lo == index 24 hi == index 25  PC == index 26
        reg.append(0)
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
        if (line[0:3] == "beq"):  # BEQ
            line = line.replace("beq", "")
            line = line.split(",")
            for i in range(len(labelName)):
                if (labelName[i] == line[2]):
                    labellocation = labelIndex[i]

            ofset = labellocation - location
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

        if (line[0:3] == "slt"):  # SLT
            line = line.replace("slt", "")
            line = line.split(",")
            rd = format(int(line[2]), '05b')
            rt = format(int(line[1]), '05b')
            rs = format(int(line[0]), '05b')
            f.write(str('000000') + str(rs) + str(rt) + str(rd) + str('00000101010') + '\n')

        if (line[0:2] == "sw"):  # SW
            line = line.replace("sw", "")
            line = line.replace("(", ",")
            line = line.replace(")", "")
            line = line.split(",")
            line2 = int(line[1]) if(int(line[1]) > 0) else (int(line[1])*-1)^65534 + 1
            imm = format(line2, '016b')
            rt = format(int(line[2]), '05b')
            rs = format(int(line[0]), '05b')
            f.write(str('101011') + str(rs) + str(rt) + str(imm) + '\n')


        if (line[0:2] == "lw"):  # LW
            line = line.replace("lw", "")
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

        if (line[0:4] == "mult"):  # MULT
            line = line.replace("mult", "")
            line = line.split(",")
            rs = format(int(line[1]), '05b')
            rt = format(int(line[0]), '05b')
            f.write(str('000000') + str(rs) + str(rt) + str('0000000000011000') + '\n')

        if (line[0:5] == "addiu"):  # ADDIU
            line = line.replace("addiu", "")
            line = line.split(",")
            imm = format(int(line[2]), '016b')
            rs = format(int(line[1]), '05b')
            rt = format(int(line[0]), '05b')
            f.write(str('001001') + str(rs) + str(rt) + str(imm) + '\n')

        if (line[0:4] == "addi"):  # ADDI
            line = line.replace("addi", "")
            line = line.split(",")
            imm = format(int(line[2]), '016b') if (int(line[2]) > 0) else format(65536 + int(line[2]), '016b')
            rs = format(int(line[1]), '05b')
            rt = format(int(line[0]), '05b')
            f.write(str('001000') + str(rs) + str(rt) + str(imm) + '\n')

        elif (line[0:3] == "add"):  # ADD
            line = line.replace("add", "")
            line = line.split(",")
            rd = format(int(line[0]), '05b')
            rs = format(int(line[1]), '05b')
            rt = format(int(line[2]), '05b')
            f.write(str('000000') + str(rs) + str(rt) + str(rd) + str('00000100000') + '\n')

        elif (line[0:1] == "j"):  # JUMP
            line = line.replace("j", "")
            line = line.split(",")

            # Since jump instruction has 2 options:
            # 1) jump to a label
            # 2) jump to a target (integer)
            # We need to save the label destination and its target location

            if (line[0].isdigit()):  # First,test to see if it's a label or a integer
                f.write(str('000010') + str(format(int(line[0]), '026b')) + '\n')

            else:  # Jumping to label
                for i in range(len(labelName)):
                    if (labelName[i] == line[0]):
                        f.write(str('000010') + str(format(int(labelIndex[i]), '026b')) + '\n')
        if location != len(asm):
            line = asm[location]
            line = ''.join(str(e) for e in line)
        j += 1

    f.close()


if __name__ == "__main__":
    main()
