     goto main
     wb 0

res  ww 0
A    ww 5
B    ww 10

hlt  halt
main += x, A
     += y, B
     mov y, res
     goto hlt