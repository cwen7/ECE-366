addi $8, $0, 0x2000
addi $10, $0, 1
addi $15,$0, 256
addi $16, $0, 1
addi $17, $0, 5
addi $18, $0, 0
addi $19, $0, 4
loop1:sb   $10, 0($8)
addi $8 , $8, 1
addi $10, $10, 1

bne  $10, $15, loop1
addi $10,$10 , -1
sb   $10, 0($8)

load:addi $8, $0, 0x2000
addi $10, $0, 256
add  $12, $0, $0

loop2:  lb   $11, 0($8)
addi  $9, $0, 0
addi $14, $0, 8

loop3:andi $13, $11, 0x01
bne  $13, $16, skip1

addi $9, $9, 1
beq  $9, $17, skip2

skip1:srl $11, $11, 1
addi $14, $14, -1
bne $14 , $18, loop3

bne  $9, $19, skip2
addi $12, $12, 1

skip2:addi $10, $10, -1
addi $8, $8, 1
bne  $10, $18, loop2




