goto main
     wb 0

res  ww 50


A    ww 0
B    ww 0
C    ww 0

hlt  halt
main += s, res
     if_zero s, hlt
     mov s, A
     mov x, res
l1   ^2 res, B
     >  B, A, C
     zera s
     += s, C
     if_zero s, l2
     goto l3
l2   += s, res
     ++ s
     mov s, res
     goto l1
l3   zera s
     += s, res
     -- s
     mov s, res
     goto hlt