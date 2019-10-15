; Push numbers from 0x0 to 0xF to the stack
            ADDI r1, r0, 0
            ADDI sp, r0, stack_pointer

push_loop:  CMPI r1, 0x10
            JE done1
            ADDI r1, r1, 1
            PUSH r1
            JMP push_loop

done1:      ADDI r1, r0, 0

pop_loop:   CMPI r1, 0x10
            JE done2
            ADDI r1, r1, 1
            POP r2
            JMP pop_loop

done2:      HALT

stack_pointer: equ 0x100