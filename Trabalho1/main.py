import ufc2x as cpu
import sys
import memory as mem
import clock as clk
import disk

def init():
    disc = 'ARQUITETURA DE COMPUTADORES - PROJETO'
    print(f'\n\n{disc} \nAUTORES:\n    * Pedro Henrique Santos Barros - 415083\n    * Joao Pedro Goncalves Rocha Ribeiro - 470895')

# LEGENDA P/ ASSEMBLE NO ARQUIVO assembler.py

# A palavra de entrada 1 está representada nos algoritmos como:

# res  ww _

# onde _ representa o valor de entrada


# COMANDOS

# QUESTAO 1 - FATORIAL DE n
# MONTAR: python3 assembler.py q1.asm q1.bin
# RODAR: python3 main.py q1.bin

# QUESTAO 1 - FATORIAL DE n
# MONTAR: python3 assembler.py q1.asm q1.bin
# RODAR: python3 main.py q1.bin

# QUESTAO 2 - n-ESIMO VALOR NA SEQUENCIA FIBONACCI
# MONTAR: python3 assembler.py q2.asm q2.bin
# RODAR: python3 main.py q2.bin

# QUESTAO 3 - VERIFICA SE n E PRIMO, 1 SE SIM, 0 SE NAO
# MONTAR: python3 assembler.py q3.asm q3.bin
# RODAR: python3 main.py q3.bin

# QUESTAO 4 - ALTURA DE UMA ARVORE BINARIA DE n NOS
# MONTAR: python3 assembler.py q4.asm q4.bin
# RODAR: python3 main.py q4.bin

init()

disk.read(str(sys.argv[1]))
print("\nExecutando Arquivo: ", str(sys.argv[1]))

print("\nEntrada Word 1: ", mem.read_word(1))
print("\nComputando...\n")
clk.start([cpu])

print("\nSaida Word 1: ", mem.read_word(1))


