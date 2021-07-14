import ufc2x as cpu
import memory as mem
import clock as clk

#dados:
mem.write_word(200, 2)
mem.write_word(201, 4)
mem.write_word(202, 500)
mem.write_word(205, 1)

###Algoritmo na memÃ³ria principal:
###- Soma dois nÃºmeros gravados nas posiÃ§Ãµes 200 e 201 da memÃ³ria.
###- Se a soma for 0, para.
###- Caso contrÃ¡rio, subtrai do resultado o valor gravado na posiÃ§Ã£o 205 da memÃ³ria.
###- Guarda o resultado na posiÃ§Ã£o 203.
###
###Em pseudo-cÃ³digo:
#
#1: X <- X + mem_word[200]
#2: X <- X + mem_word[201]
#3: IF X = 0 GOTO 15       (VÃ¡ para Byte 15 = VÃ¡ para linha 8 do algoritmo)
#4: GOTO 11                (VÃ¡ para Byte 11 = VÃ¡ para linha 6 do algoritmo)
#5: X <- X + mem_word[201] (Esta linha nunca Ã© executada. EstÃ¡ aqui apenas para demonstrar o salto realizado pelo GOTO)
#6: X <- X - mem_word[205]
#7: mem_word[203] <- X
#8: HALT

#Programa escrito em linguagem de mÃ¡quina direto na memÃ³ria principal
mem.write_byte(1, 2)    #X <- X +
mem.write_byte(2, 200)  #mem_word[200]
mem.write_byte(3, 2)    #X <- X +
mem.write_byte(4, 201)  #mem_word[201]
mem.write_byte(5, 11)   #IF X = 0 GOTO
mem.write_byte(6, 15)   #15
mem.write_byte(7, 9)    #GOTO
mem.write_byte(8, 11)   #11
mem.write_byte(9, 2)    #X <- X +
mem.write_byte(10, 201) #mem_word[201]
mem.write_byte(11, 13)  #X <- X -
mem.write_byte(12, 205) #mem_word[205]
mem.write_byte(13, 6)   #mem_word[address] <- X
mem.write_byte(14, 203) #address
mem.write_byte(15, 255) #HALT

print("Antes: ", mem.read_word(203))

clk.start([cpu])

print("Depois: ", mem.read_word(203))

