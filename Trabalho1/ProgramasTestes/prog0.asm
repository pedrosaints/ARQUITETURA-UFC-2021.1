     goto main
     wb 0

res  ww 1
A    ww 5
B    ww 10

hlt  halt
main += v, B
     -= v, A
     ++ v
loop -- v
     if_zero  v, end
     goto loop
end  mov v, res
     goto hlt