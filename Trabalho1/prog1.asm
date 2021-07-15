     goto main
     wb 0

res  ww 0
A    ww 5

hlt  halt
main += x, A
loop -- x
     if_zero  x, end
     goto loop
end  mov x, res
     goto hlt