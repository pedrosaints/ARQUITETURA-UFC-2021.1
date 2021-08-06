goto main
     wb 0

res  ww 12


A    ww 1
B    ww 0

hlt  halt
main += s, res
     if_zero s, hlt
     -- s
     if_zero s, hlt
     -- s
     ++ x
     if_zero s, end
loop mov x, B
     += x, A
     -- s
     mov x, res
     if_zero s, hlt
     zera y
     += y, B
     mov y, A
     goto loop
end mov x, res