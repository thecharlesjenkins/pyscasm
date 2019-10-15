switch_addr: equ 0xFF
led_addr: equ 0xFF

loop:
IN r1, switch_addr
OUT r1, led_addr
JMP loop