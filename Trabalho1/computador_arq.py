import ufc2x as cpu
import sys
import memory as mem
import clock as clk
import disk

def init():
    disc = 'ARQUITETURA DE COMPUTADORES - PROJETO'
    print(f'AUTOR: Pedro H Santos B, {disc} \n')  # Press Ctrl+F8 to toggle the breakpoint.

init()

# ANOTAÇOES
# firmware[X] = 0b 000000100 000 00 111100 01000000 000 000
#                   NEXT_I   JAM NZ  ALU     REG  M_IO R_Reg

# COMANDO
# montar: python3 assembler.py prog0.asm prog0.bin
# rodar: python3 computador_arq.py prog0.bin

disk.read(str(sys.argv[1]))

print("Antes: ", mem.read_word(1))

clk.start([cpu])

print("Depois: ", mem.read_word(1))


