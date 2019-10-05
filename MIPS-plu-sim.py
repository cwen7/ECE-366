memory = []
g = 0
for i in range(1025):
    g = g + 1
    mem = hex(4096*2 + i*4)
    memory.append([mem, 0, 0, 0, 0])
    print(memory[i]) if (g == 8) else print(memory[i], end=" ")
    if(g == 8):
        g=0
