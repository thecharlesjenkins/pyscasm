                addi sp, r0, stack
begin:          addi r1, r0, 0
fib_call_loop:  CMPI r1, max_iters
                JE begin
                call fib
                out r2, led_addr
                addi r1, r1, 1
                JMP fib_call_loop

org 0x10
; Calculates the nth fibonacci number
; n passed in through r1
;
; Returns value in r2
;

; int fib(int n)
; {
;   if (n <= 1) {
;       return 1;
;   }
;   return fib(n-1) + fib(n-2)
;

fib:            cmpi r1, 1
                jle  base_case
                ; n > 1
    loop:       push r1
                ; Call fib(n-1)
                addi r1, r1, -1
                call fib
                pop r1
                push r2
                push r1

                ; Call fib(n-2)
                addi r1, r1, -2
                call fib
                pop r1
                pop r3
                add r2, r2, r3
                ret
    base_case:  addi r2, r0, 1
                ret


max_iters: equ 0xF
led_addr: equ 0xFF
stack: equ 0x100
