ADDI r1, r0, 0  ; int x1 = 0 (smaller)
ADDI r2, r0, 1  ; int x2 = 1 (larger)

ADDI r3, r0, 10 ; int iterations = 10

loop:
JE done

ADD r1, r1, r2  ; x1 = x1 + x2
XCHG r1, r2     ; x1, x2 = x2, x1
OUT r2, 0xFF
ADDI r3, r3, -1  ; Load flags for r3

JMP loop

done:
ADD r4, r0, r2  ; r4 = r2
HALT

; 0 1 1 2 3 5 8
