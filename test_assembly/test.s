;thing: equ 0x89
;org 50
;ADDI r1, r0, 0x01
;dw 0x78
;one: ADDI r2, r1, two
;ADDI r3, r2, 0x03
;two: ADDI r4, r3, 0x04
;org thing
;ADD r7, r6, r5
;
;bye: equ 50 ; lol
ADD r7, r3, r1
ADDI r7, r3, 0xcafe
