        ORG     &H000       ; Lmao
Start:  LOAD    B
        ADD     C
        STORE   A
Here:   JUMP    Here

        ORG     &H010
A:      DW      &H0000
B:      DW      &H0004
C:      DW      &H0003
D:      DW      &H0000
