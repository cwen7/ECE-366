addi $8, $0, 0x2000
addi $10, $0, 1
addi $15, $0, 1
addi $16, $0, 5
addi $17, $0, 256
addi $18, $0, 4
addi $19, $0, 0

addi $20, $0, 0x2120

loop1:
sb   $10, 0($8)
addi $8 , $8, 1
addi $10, $10, 1

bne  $10, $17, loop1
addi $10, $10 , -1
sb   $10, 0($8)

addi $8, $0, 0x2000
addi $10, $10, 1# $10 as a counter 256
add  $12, $0, $0



search:
lb $11, 0($8)
addi $9, $0, 0#$count 1
addi $13, $0, 8#$13 count 8 times

countOne:
andi $14, $11, 1
bne $14, $15, notOne

addi $9, $9, 1
beq $9, $16, exit#more than 4

notOne:
srl $11, $11, 1
addi $13, $13, -1
bne $13, $0, countOne


bne $9, $18, exit
addi $19, $19, 1

exit:
addi $10, $10, -1
addi $8, $8, 1
bne  $10, $0, search

sw $19, 0($20)