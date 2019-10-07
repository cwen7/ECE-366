


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
        #print(j, line)

        if (line[0:4] == "addi"):  # ADDI
            line = line.replace("addi", "")
            line = line.split(",")
            if line[2][0:2] == "0x" or line[2][0:3] == "-0x":
                line[2] = line[2].replace("0x", "")
                imm = format(int(line[2], 16), '04x') if (int(line[2]) > 0) else format(int(line[2], 16), '04x')
            else:
                imm = format(int(line[2]), '04x')



            print(int(line[2], 16))

            print(imm)
            imm = int(imm, 16) + 1
            imm = imm + 1
            imm = format(imm, '04x')
            print(imm)

            rs = format(int(line[1]), '05b')
            rt = format(int(line[0]), '05b')
            f.write(str('001000') + str(rs) + str(rt) + str(imm) + '\n')

        if location != len(asm):
            line = asm[location]
            line = ''.join(str(e) for e in line)
        j += 1

    f.close()


if __name__ == "__main__":
    main()
