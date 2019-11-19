        ORG     &H000       ; Lmao
        JUMP Start
        RETI
        JUMP IRQ1
        RETI
        RETI
Start:  SEI &HF
        LOAD    B
        ADD     C
        STORE   A
        OUT &H10
Here:   JUMP    Here

IRQ1:   LOADI &H69
        OUT &H69
        RETI

        ORG     &H010
A:      DW      &H0000
B:      DW      &H0004
C:      DW      &H0003
D:      DW      &H0000
