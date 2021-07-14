import ufc2x as cpu
import sys
import memory as mem
import clock as clk
import disk

# COMANDO
# montar: python3 assembler.py prog0.asm prog0.bin
# rodar: python3 computador_arq.py prog0.bin

disk.read(str(sys.argv[1]))

print("Antes: ", mem.read_word(1))

clk.start([cpu])

print("Depois: ", mem.read_word(1))


