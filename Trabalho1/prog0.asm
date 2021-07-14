     goto main
     wb 0

res  ww 0
A    ww 256
B    ww 301
c1   ww 1

main += x, A
     += x, B
     if_zero  x, jmp
     mov x, res
hlt  halt
jmp  += x, c1
     mov x, res
     goto hlt