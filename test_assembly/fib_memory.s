                ADDI r1, r0, 0  ; int x1 = 0 (smaller)
                ADDI r2, r0, 1  ; int x2 = 1 (larger)

                ADDI r3, r0, iterations ; int iterations = 10

                ADDI r4, r0, 0 ; array index

loop:           CMP r3, r0
                JE done

                ADD r1, r1, r2      ; x1 = x1 + x2
                XCHG r1, r2         ; x1, x2 = x2, x1
                SW r2, r4, array    ; array[r4] = x2

                ADDI r4, r4, 1      ; r4++
                ADDI r3, r3, -1     ; Load flags for r3
                JMP loop

done:           ADDI r4, r0, 0

display_loop:   CMPI r4, iterations
                JE done

                LW r1, r4, array
                OUT r1, led_addr

                ADDI r4, r4, 1

                JMP display_loop

iterations: equ 0x10
array: equ 0x100
led_addr: equ 0xFF
