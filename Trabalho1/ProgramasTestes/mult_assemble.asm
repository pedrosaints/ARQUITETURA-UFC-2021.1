goto main
     wb 0

res  ww 0
A    ww 19
B    ww 13

hlt  halt
main += y, B
loop if_zero y, end
     += x, A
     -- y
     goto loop
end  mov x, res
     goto hlt