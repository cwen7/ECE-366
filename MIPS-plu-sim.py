memory = []
g = 0
for i in range(1025):
    g = g + 1
    mem = hex(4096*2 + i*4)
    memory.append([mem, 0, 0, 0, 0])
    # print(memory[i]) if (g == 8) else print(memory[i], end=" ")

    if g == 8:
        g = 0
print()
reg = [0]
for i in range(27):         # lo == index 24 hi == index 25  PC == index 26
    reg.append(0)
    print(i, reg[i]) if (i < 24) else print(i, reg[i], 'reg or pc')

# this will make accessing lo, hi, pc easy to remember

lo = 24  # reg[lo]
hi = 25  # reg[hi]
pc = 26  # reg[pc]

