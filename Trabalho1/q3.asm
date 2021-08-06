goto main
     wb 0

res  ww 23


A    ww 0
P    ww 1
D    ww 2
M    ww 0
C1   ww 1

hlt  halt
main += s, res
     mov x, res
     mov s, A
     if_zero s, hlt
     -- s
     if_zero s, hlt
l1   *  P, D, M
     =  M, A, res
     zera s
     += s, res
     if_zero s, l2
     =  P, C1, res
     goto hlt
l2   >  M, A, res
     += s, res
     if_zero s, l3
     goto l4
l3   += s, P
     ++ s
     mov s, P
     goto l1
l4   =  D, A, res
     zera s
     += s, res
     if_zero s, l5
     goto hlt
l5   += s, D
     ++ s
     mov s, D
     zera s
     ++ s
     mov s, P
     goto l1