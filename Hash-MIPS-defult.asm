lui $8, 0xFA19
ori $8, $8, 0xE366
ori $9, $9, 0x0001
ori $16, $16, 0x2000
ori $17, $17, 0x2020
ori $19, $19, 1
ori $20, $20, 101
ori $23, $23, 0x1F

loop:multu $9, $8
mfhi $11
mflo $10 
xor $12, $11, $10

multu $12, $8
mfhi $11
mflo $10 
xor $12, $11, $10

multu $12, $8
mfhi $11
mflo $10 
xor $12, $11, $10

multu $12, $8
mfhi $11
mflo $10 
xor $12, $11, $10

multu $12, $8
mfhi $11
mflo $10 
xor $12, $11, $10

ori $13, $13, 0xFFFF
ori $14, $14, 0x00FF


and $15, $13, $12
srl $12, $12, 16
xor $12, $15, $12


and $15, $14, $12
srl $12, $12, 8
xor $12, $15, $12  



sh $12, 0($17)

ori $21, $12, 0

and $22, $21, $23
srl $21, $21, 1
beq $22, $23, thereIs5

and $22, $21, $23
srl $21, $21, 1
beq $22, $23, thereIs5

and $22, $21, $23
srl $21, $21, 1
beq $22, $23, thereIs5

and $22, $21, $23
bne $22, $23, no5ones

thereIs5:lbu $22, 8($16)
addi $22, $22, 1
sh $22, 8($16)

no5ones:lbu $18, 4($16)
sltu $18, $18, $12
bne $18, $19, skip

sh $17, 0($16)
sh $12, 4($16)

skip:addi $17, $17, 2
addi $9, $9, 1

bne $9, $20, loop
