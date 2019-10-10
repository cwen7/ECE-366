addi $22, $22, 1
lui $8, 0xFA19
lui $8, 0xFA19
ori $8, $8, 0xE366
sh $8, 0x2002($17)
sb $8, 0x2005($17)
skip: and $15, $14, $12
loop:addi $8, $0, 2000
lbu $22, 0x2005($0)
lb $22, 0x2005($0)

addi $10, $0, 9
addi $11, $0, 10
multu $10, $11
mflo $12
mfhi $13