import ufc2x as cpu
import sys
import memory as mem
import clock as clk
import disk

def init():
    disc = 'ARQUITETURA DE COMPUTADORES - PROJETO'
    print(f'\n\n{disc} \nAUTORES:\n    * Pedro Henrique Santos Barros - 415083\n    * Joao Pedro Goncalves Rocha Ribeiro - 470895')

# ANOTAÇOES
# firmware[X] = 0b 000000100 000 00 111100 01000000 000 000
#                   NEXT_I   JAM NZ  ALU     REG  M_IO R_Reg

# COMANDO
# montar: python3 assembler.py prog0.asm prog0.bin
# rodar: python3 computador_arq.py prog0.bin

init()

disk.read(str(sys.argv[1]))
print("\nExecutando Arquivo: ", str(sys.argv[1]))

print("\nEntrada Word 1: ", mem.read_word(1))
print("\nComputando...\n")
clk.start([cpu])

print("\nSaida Word 1: ", mem.read_word(1))


