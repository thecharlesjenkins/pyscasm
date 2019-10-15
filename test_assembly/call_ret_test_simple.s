        addi sp, r0, stack
        call do_add
        out r1, led_addr
        halt

do_add: addi r1, r0, 0x69
        ret

stack: equ 0x100
led_addr: equ 0xFF
