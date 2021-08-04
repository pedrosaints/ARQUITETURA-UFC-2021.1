from array import array
import memory
import numpy as np
int64 = 0
int64 = np.dtype('int64').type(int64)

MIR = 0
MPC = 0

MAR = 0
MDR = 0
PC = 0
MBR = 0
X = 0
Y = 0
V = 0
H = 0

N = 0
Z = 1

BUS_A = 0
BUS_B = 0
BUS_C = 0

firmware = [int64] * 512

# main        0b000000000 100 00 110101 001000 001 001
firmware[0] = 0b000000000100001101010010000001001
# PC <- PC + 1; MBR <- read_byte(PC); GOTO MBR;

# X = X + mem[address]
firmware[2] = 0b000000011000001101010010000001001
# PC <- PC + 1; MBR <- read_byte(PC); GOTO 3
firmware[3] = 0b000000100000000101001000000010010
# MAR <- MBR; read_word; GOTO 4
firmware[4] = 0b000000101000000101000000010000000
# H <- MDR; GOTO 5
firmware[5] = 0b000000000000001111000001000000011
# X <- X + H; GOTO MAIN;

# mem[address] = X
firmware[6] = 0b000000111000001101010010000001001
# PC <- PC + 1; fetch; GOTO 7
firmware[7] = 0b000001000000000101001000000000010
# MAR <- MBR; GOTO 8
firmware[8] = 0b000000000000000101000100000100011
# MDR <- X; write; GOTO MAIN

# goto address
firmware[9] = 0b000001010000001101010010000001001
# PC <- PC + 1; fetch; GOTO 10
firmware[10] = 0b000000000100000101000010000001010
# PC <- MBR; fetch; GOTO MBR;

# if X = 0 goto address
firmware[11] = 0b000001100001000101000001000000011
# X <- X; IF ALU = 0 GOTO 268 (100001100) ELSE GOTO 12 (000001100);
firmware[12] = 0b000000000000001101010010000000001
# PC <- PC + 1; GOTO MAIN;
firmware[268] = 0b100001101000001101010010000001001
# PC <- PC + 1; fetch; GOTO 269
firmware[269] = 0b000000000100000101000010000001010
# PC <- MBR; fetch; GOTO MBR;

# X = X - mem[address]
firmware[13] = 0b000001110000001101010010000001001
# PC <- PC + 1; fetch;
firmware[14] = 0b000001111000000101001000000010010
# MAR <- MBR; read;
firmware[15] = 0b000010000000000101000000010000000
# H <- MDR;
firmware[16] = 0b000000000000001111110001000000011
# X <- X - H; GOTO MAIN;

# X = X + 1
firmware[17] = 0b000000000000001101010001000000011
# X <- X + 1; GOTO MAIN;

# X = X - 1
firmware[18] = 0b000000000000001101100001000000011
# X <- X - 1; GOTO MAIN;

# Y = Y + mem[address]
firmware[19] = 0b000010100000001101010010000001001
# PC <- PC + 1; MBR <- read_byte(PC); GOTO 20
firmware[20] = 0b000010101000000101001000000010010
# MAR <- MBR; read_word; GOTO 21
firmware[21] = 0b000010110000000101000000010000000
# H <- MDR; GOTO 22
firmware[22] = 0b000000000000001111000000100000100
# Y <- Y + H; GOTO MAIN;

# Y = Y + 1
firmware[23] = 0b000000000000001101010000100000100
# Y <- Y + 1; GOTO MAIN;

# Y = Y - 1
firmware[24] = 0b000000000000001101100000100000100
# Y <- Y - 1; GOTO MAIN;

# Y = Y - mem[address]
firmware[25] = 0b000001110000001101010010000001001
# PC <- PC + 1; fetch;
firmware[26] = 0b000001111000000101001000000010010
# MAR <- MBR; read;
firmware[27] = 0b000010000000000101000000010000000
# H <- MDR;
firmware[28] = 0b000000000000001111110000100000100
# Y <- Y - H; GOTO MAIN;

# mem[address] = Y
firmware[29] = 0b000011110000001101010010000001001
# PC <- PC + 1; fetch; GOTO 30
firmware[30] = 0b000011111000000101001000000000010
# MAR <- MBR; GOTO 31
firmware[31] = 0b000000000000000101000100000100100
# MDR <- Y; write; GOTO MAIN

# if Y = 0 goto address
firmware[32] = 0b000100001001000101000000100000100
# Y <- Y; IF ALU = 0 GOTO 289 (100100001) ELSE GOTO 33 (000100001);
firmware[33] = 0b000000000000001101010010000000001
# PC <- PC + 1; GOTO MAIN;
firmware[289] = 0b100100010000001101010010000001001
# PC <- PC + 1; fetch; GOTO 290
firmware[290] = 0b000000000100000101000010000001010
# PC <- MBR; fetch; GOTO MBR;

# if Y = 0 goto address
firmware[34] = 0b000100011001000101000000100000100
# Y <- Y; IF ALU = 0 GOTO 291 (100100011) ELSE GOTO 35 (000100011);
firmware[35] = 0b000100100000001101100000100000100
# Y <- Y - 1; GOTO MAIN;
firmware[36] = 0b000100101000000101000000010000101
# H <- V; GOTO 37
firmware[37] = 0b000100010000001111000001000000011
# X <- X + H; GOTO 34;
firmware[291] = 0b00000000000000110101000000000111

# V = V + mem[address]
firmware[38] = 0b000100111000001101010010000001001
# PC <- PC + 1; MBR <- read_byte(PC); GOTO 39
firmware[39] = 0b000101000000000101001000000010010
# MAR <- MBR; read_word; GOTO 40
firmware[40] = 0b000101001000000101000000010000000
# H <- MDR; GOTO 41
firmware[41] = 0b000000000000001111000000001000101
# V <- V + H; GOTO MAIN;

def read_regs(reg_num):
    global BUS_A, BUS_B, H, MDR, PC, MBR, X, Y, V

    BUS_A = H

    if reg_num == 0:
        BUS_B = MDR
    elif reg_num == 1:
        BUS_B = PC
    elif reg_num == 2:
        BUS_B = MBR
    elif reg_num == 3:
        BUS_B = X
    elif reg_num == 4:
        BUS_B = Y
    elif reg_num == 5:
        BUS_B = V
    else:
        BUS_B = 0


def write_regs(reg_bits):
    global MAR, MDR, PC, X, Y, H, V, BUS_C

    if reg_bits & 0b1000000:
        MAR = BUS_C
    if reg_bits & 0b0100000:
        MDR = BUS_C
    if reg_bits & 0b0010000:
        PC = BUS_C
    if reg_bits & 0b0001000:
        X = BUS_C
    if reg_bits & 0b0000100:
        Y = BUS_C
    if reg_bits & 0b0000010:
        H = BUS_C
    if reg_bits & 0b0000001:
        V = BUS_C


def alu(control_bits):
    global N, Z, BUS_A, BUS_B, BUS_C

    a = BUS_A
    b = BUS_B
    o = 0

    shift_bits = (0b11000000 & control_bits) >> 6
    control_bits = 0b00111111 & control_bits

    if control_bits == 0b011000:
        o = a
    elif control_bits == 0b010100:
        o = b
    elif control_bits == 0b011010:
        o = ~a
    elif control_bits == 0b101100:
        o = ~b
    elif control_bits == 0b111100:
        o = a + b
    elif control_bits == 0b111101:
        o = a + b + 1
    elif control_bits == 0b111001:
        o = a + 1
    elif control_bits == 0b110101:
        o = b + 1
    elif control_bits == 0b111111:
        o = b - a
    elif control_bits == 0b110110:
        o = b - 1
    elif control_bits == 0b111011:
        o = -a
    elif control_bits == 0b001100:
        o = a & b
    elif control_bits == 0b011100:
        o = a | b
    elif control_bits == 0b010000:
        o = 0
    elif control_bits == 0b110001:
        o = 1
    elif control_bits == 0b110010:
        o = -1

    if o == 0:
        N = 0
        Z = 1
    else:
        N = 1
        Z = 0

    if shift_bits == 0b01:
        o = o << 1
    elif shift_bits == 0b10:
        o = o >> 1
    elif shift_bits == 0b11:
        o = o << 8

    BUS_C = o


def next_instruction(next, jam):
    global MPC, MBR, Z, N

    if jam == 0:
        MPC = next
        return

    if jam & 0b001:
        next = next | (Z << 8)

    if jam & 0b010:
        next = next | (N << 8)

    if jam & 0b100:
        next = next | MBR

    MPC = next


def memory_io(mem_bits):
    global PC, MBR, MDR, MAR

    if mem_bits & 0b001:
        MBR = memory.read_byte(PC)

    if mem_bits & 0b010:
        MDR = memory.read_word(MAR)

    if mem_bits & 0b100:
        memory.write_word(MAR, MDR)


def step():
    global MIR, MPC

    MIR = firmware[MPC]

    if MIR == 0:
        return False

    read_regs(MIR & 0b000000000000000000000000000000111)
    alu((MIR & 0b000000000000111111110000000000000) >> 13)
    write_regs((MIR & 0b000000000000000000001111111000000) >> 6)
    memory_io((MIR & 0b000000000000000000000000000111000) >> 3)
    next_instruction((MIR & 0b111111111000000000000000000000000) >> 24,
                     (MIR & 0b000000000111000000000000000000000) >> 21)

    return True










