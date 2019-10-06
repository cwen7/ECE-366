


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
    h = open("mips.asm", "r")
    asm = h.readlines()
    for item in range(asm.count('\n')):  # Remove all empty lines '\n'
        asm.remove('\n')

    saveJumpLabel(asm, labelIndex, labelName)  # Save all jump's destinations

    # this block of code allocates all the memory for address ranging from 0x2000 - 0x3000 if you uncomment the commented area and run it you will see
    memory = []
    g = 0
    for i in range(1025):
        mem = hex(4096 *2 + i* 4)
        memory.append([mem, 0, 0, 0, 0])
        ##g = g + 1
        ##print(memory[i]) if (g == 8) else print(memory[i], end=" ")
        if g == 8:
            g = 0
    # uncomenting this gives you a space to raed the out put more claerly
    ##print()

    # this block creates ann array for all the registers and at the same time it allocates space for lo hi and pc
    reg = [0]
    for i in range(27):  # lo == index 24 hi == index 25  PC == index 26
        reg.append(0)
        ##print(i, reg[i]) if (i < 24) else print(i, reg[i], 'reg or pc')

    # this will make accessing lo, hi, pc easy to remember
    lo = 24  # reg[lo]
    hi = 25  # reg[hi]
    pc = 26  # reg[pc]

    f.close()


if __name__ == "__main__":
    main()
