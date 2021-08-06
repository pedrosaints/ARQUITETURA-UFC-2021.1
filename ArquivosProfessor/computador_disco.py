
import ufc2x as cpu
import memory as mem
import clock as clk
import disk

disk.read('prog0.bin')

print("Antes: ", mem.read_word(1))

clk.start([cpu])

print("Depois: ", mem.read_word(1))

