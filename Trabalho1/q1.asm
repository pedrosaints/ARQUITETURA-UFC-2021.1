goto main
     wb 0

res  ww 10


A    ww 0

hlt  halt
main += s, res
     if_zero  s, end
loop -- s
     if_zero  s, hlt
     mov s, A
     *  res, A, res
     goto loop
end  ++ s
     mov s, res
     goto hlt