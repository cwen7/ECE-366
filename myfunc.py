
if (line[0:3] == "ori"):  # ORI
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

    if rt != 0:
        reg[rt] = rs | imm
        reg[rt] = format(reg[rt], '08x')
    #print(reg[rt], "ori")

---------------------------------------------------------
if (line[0:3] == "xor"):  # XOR
    line = line.replace("xor", "")
    line = line.split(",")
    rd = int(line[0], 10)
    rs = int(line[1], 10)
    rt = int(line[2], 10)
    rs = int(reg[rs], 16)
    rt = int(reg[rt], 16)
    print(reg[rs])
    if rd != 0:
        reg[rd] = format(rs ^ rt, '08x')
    #print(reg[rd], "xor")
---------------------------------------------------------
if (line[0:3] == "add"):  # ADD
    if (line[0:3] == "add"):  # ADD
        line = line.replace("add", "")
        line = line.split(",")
        rd = int(line[0], 10)
        rs = int(line[1], 10)
        rt = int(line[2], 10)
        rs = int(reg[rs], 16)
        rt = int(reg[rt], 16)

        if rs > 2 ** 31 - 1:
            rs = reg[rs] - 2 ** 32

        if rd != 0:
            reg[rd] = format(rs + rt, '08x')

       # print(reg[rd], "add")
---------------------------------------------------------
if (line[0:4] == "andi"):  # ANDI
    line = line.replace("andi", "")
    line = line.split(",")

    if line[2][0:2] == "0x" or line[2][0:3] == "-0x":
        line[2] = line[2].replace("0x", "")
        imm = int(line[2], 16)
    else:
        imm = int(line[2], 10)
    rs = int(line[1])
    rt = int(line[0])
    rs = int(reg[rs], 16)

    if rt != 0:
        reg[rt] = rs & imm
        reg[rt] = format(reg[rt], '08x')
    #print(reg[rt], "andi")
---------------------------------------------------------
if (line[0:4] == "sltu"):  # SLTU
    line = line.replace("sltu", "")
    line = line.split(",")
    rd = int(line[0], 10)
    rs = int(line[1], 10)
    rt = int(line[2], 10)
    rs = int(reg[rs], 16)
    rt = int(reg[rt], 16)
    # print(reg[rs])

    if reg[rs] < reg[rt]:
        reg[rd] = '1'
    else:
        reg[rd] = '0'
---------------------------------------------------------
if (line[0:5] == "multu"):  # MULTU
    line = line.replace("multu", "")
    line = line.split(",")
    rs = int(line[0], 10)
    rt = int(line[1], 10)
    rs = int(reg[rs], 16)
    rt = int(reg[rt], 16)

    if rs > 2 ** 31 - 1:
        rs = reg[rs] - 2 ** 32

    if lo != 0:
        reg[lo] = format(reg[rs] * reg[rt], '08x')
    #print(reg[lo], "multu")

---------------------------------------------------------
if (line[0:4] == "mflo"):  # MFLO
    line = line.replace("mflo", "")
    line = line.split(",")
    rd = int(line[0], 10)

    if rd != 0:
        reg[rd] = format(reg[lo], '08x')
---------------------------------------------------------
if (line[0:4] == "mfhi"):  # MFHI
    line = line.replace("mfhi", "")
    line = line.split(",")
    rd = int(line[0], 10)

    if rd != 0:
        reg[rd] = format(reg[hi], '08x')

