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
S = 0
H = 0

N = 0
Z = 1

BUS_A = 0
BUS_B = 0
BUS_C = 0

firmware = [int64] * 512

# main        0b000000000 100 00 110101 00100000 001 001
firmware[0] = 0b0000000001000011010100100000001001
# PC <- PC + 1; MBR <- read_byte(PC); GOTO MBR;

# X = X + mem[address]
firmware[2] = 0b0000000110000011010100100000001001
# PC <- PC + 1; MBR <- read_byte(PC); GOTO 3
firmware[3] = 0b0000001000000001010010000000010010
# MAR <- MBR; read_word; GOTO 4
firmware[4] = 0b0000001010000001010000000100000000
# H <- MDR; GOTO 5
firmware[5] = 0b0000000000000011110000010000000011
# X <- X + H; GOTO MAIN;

# mem[address] = X
firmware[6] = 0b0000001110000011010100100000001001
# PC <- PC + 1; fetch; GOTO 7
firmware[7] = 0b0000010000000001010010000000000010
# MAR <- MBR; GOTO 8
firmware[8] = 0b0000000000000001010001000000100011
# MDR <- X; write; GOTO MAIN

# goto address
firmware[9] = 0b0000010100000011010100100000001001
# PC <- PC + 1; fetch; GOTO 10
firmware[10] = 0b0000000001000001010000100000001010
# PC <- MBR; fetch; GOTO MBR;

# if X = 0 goto address
firmware[11] = 0b0000011000010001010000010000000011
# X <- X; IF ALU = 0 GOTO 268 (100001100) ELSE GOTO 12 (000001100);
firmware[12] = 0b0000000000000011010100100000000001
# PC <- PC + 1; GOTO MAIN;
firmware[268] = 0b1000011010000011010100100000001001
# PC <- PC + 1; fetch; GOTO 269
firmware[269] = 0b0000000001000001010000100000001010
# PC <- MBR; fetch; GOTO MBR;

# X = X - mem[address]
firmware[13] = 0b0000011100000011010100100000001001
# PC <- PC + 1; fetch;
firmware[14] = 0b0000011110000001010010000000010010
# MAR <- MBR; read;
firmware[15] = 0b0000100000000001010000000100000000
# H <- MDR;
firmware[16] = 0b0000000000000011111100010000000011
# X <- X - H; GOTO MAIN;

# X = X + 1
firmware[17] = 0b0000000000000011010100010000000011
# X <- X + 1; GOTO MAIN;

# X = X - 1
firmware[18] = 0b0000000000000011011000010000000011
# X <- X - 1; GOTO MAIN;

# Y = Y + mem[address]
firmware[19] = 0b0000101000000011010100100000001001
# PC <- PC + 1; MBR <- read_byte(PC); GOTO 20
firmware[20] = 0b0000101010000001010010000000010010
# MAR <- MBR; read_word; GOTO 21
firmware[21] = 0b0000101100000001010000000100000000
# H <- MDR; GOTO 22
firmware[22] = 0b0000000000000011110000001000000100
# Y <- Y + H; GOTO MAIN;

# Y = Y + 1
firmware[23] = 0b0000000000000011010100001000000100
# Y <- Y + 1; GOTO MAIN;

# Y = Y - 1
firmware[24] = 0b0000000000000011011000001000000100
# Y <- Y - 1; GOTO MAIN;

# Y = Y - mem[address]
firmware[25] = 0b0000110100000011010100100000001001
# PC <- PC + 1; fetch;
firmware[26] = 0b0000110110000001010010000000010010
# MAR <- MBR; read;
firmware[27] = 0b0000111000000001010000000100000000
# H <- MDR;
firmware[28] = 0b0000000000000011111100001000000100
# Y <- Y - H; GOTO MAIN;

# mem[address] = Y
firmware[29] = 0b0000111100000011010100100000001001
# PC <- PC + 1; fetch; GOTO 30
firmware[30] = 0b0000111110000001010010000000000010
# MAR <- MBR; GOTO 31
firmware[31] = 0b0000000000000001010001000000100100
# MDR <- Y; write; GOTO MAIN

# if Y = 0 goto address
firmware[32] = 0b0001000010010001010000001000000100
# Y <- Y; IF ALU = 0 GOTO 289 (100100001) ELSE GOTO 33 (000100001);
firmware[33] = 0b0000000000000011010100100000000001
# PC <- PC + 1; GOTO MAIN;
firmware[289] = 0b1001000100000011010100100000001001
# PC <- PC + 1; fetch; GOTO 290
firmware[290] = 0b0000000001000001010000100000001010
# PC <- MBR; fetch; GOTO MBR;

# X <- X * Y
firmware[34] = 0b0001000110010001010000001000000100
# Y <- Y; IF ALU = 0 GOTO 291 (100100011) ELSE GOTO 35 (000100011);
firmware[35] = 0b0001001000000011011000001000000100
# Y <- Y - 1; GOTO 36;
firmware[36] = 0b0001001010000001010000000100000101
# H <- V; GOTO 37
firmware[37] = 0b0001000100000011110000010000000011
# X <- X + H; GOTO 34;
firmware[291] = 0b000000000000001101010000000000111
# GOTO MAIN;

# V = V + mem[address]
firmware[38] = 0b0001001110000011010100100000001001
# PC <- PC + 1; MBR <- read_byte(PC); GOTO 39
firmware[39] = 0b0001010000000001010010000000010010
# MAR <- MBR; read_word; GOTO 40
firmware[40] = 0b0001010010000001010000000100000000
# H <- MDR; GOTO 41
firmware[41] = 0b0000000000000011110000000010000101
# V <- V + H; GOTO MAIN;

# V = V + 1
firmware[42] = 0b0000000000000011010100000010000101
# V <- V + 1; GOTO MAIN;

# V = V - 1
firmware[43] = 0b0000000000000011011000000010000101
# V <- V - 1; GOTO MAIN;

# V = V - mem[address]
firmware[44] = 0b0001011010000011010100100000001001
# PC <- PC + 1; fetch;
firmware[45] = 0b0001011100000001010010000000010010
# MAR <- MBR; read;
firmware[46] = 0b0001011110000001010000000100000000
# H <- MDR;
firmware[47] = 0b0000000000000011111100000010000101
# V <- V - H; GOTO MAIN;

# mem[address] = V
firmware[48] = 0b0001100010000011010100100000001001
# PC <- PC + 1; fetch; GOTO 49
firmware[49] = 0b0001100100000001010010000000000010
# MAR <- MBR; GOTO 50
firmware[50] = 0b0000000000000001010001000000100101
# MDR <- V; write; GOTO MAIN

# if V = 0 goto address
firmware[51] = 0b0001101000010001010000000010000101
# V <- V; IF ALU = 0 GOTO 308 (100110100) ELSE GOTO 52 (000110100);
firmware[52] = 0b0000000000000011010100100000000001
# PC <- PC + 1; GOTO MAIN;
firmware[308] = 0b1001101010000011010100100000001001
# PC <- PC + 1; fetch; GOTO 290
firmware[309] = 0b0000000001000001010000100000001010
# PC <- MBR; fetch; GOTO MBR;

# S = S + mem[address]
firmware[53] = 0b0001101100000011010100100000001001
# PC <- PC + 1; MBR <- read_byte(PC); GOTO 54
firmware[54] = 0b0001101110000001010010000000010010
# MAR <- MBR; read_word; GOTO 55
firmware[55] = 0b0001110000000001010000000100000000
# H <- MDR; GOTO 56
firmware[56] = 0b0000000000000011110000000001000110
# S <- S + H; GOTO MAIN;

# S = S - mem[address]
firmware[57] = 0b0001110100000011010100100000001001
# PC <- PC + 1; fetch;
firmware[58] = 0b0001110110000001010010000000010010
# MAR <- MBR; read;
firmware[59] = 0b0001111000000001010000000100000000
# H <- MDR;
firmware[60] = 0b0000000000000011111100000001000110
# S <- S - H; GOTO MAIN;

# S = S + 1
firmware[61] = 0b0000000000000011010100000001000110
# S <- S + 1; GOTO MAIN;

# S = S - 1
firmware[62] = 0b0000000000000011011000000001000110
# S <- S - 1; GOTO MAIN;

# mem[address] = S
firmware[63] = 0b0010000000000011010100100000001001
# PC <- PC + 1; fetch; GOTO 64
firmware[64] = 0b0010000010000001010010000000000010
# MAR <- MBR; GOTO 65
firmware[65] = 0b0000000000000001010001000000100110
# MDR <- S; write; GOTO MAIN

# if S = 0 goto address
firmware[66] = 0b0010000110010001010000000001000110
# S <- S; IF ALU = 0 GOTO 323 (101000011) ELSE GOTO 67 (001000011);
firmware[67] = 0b0000000000000011010100100000000001
# PC <- PC + 1; GOTO MAIN;
firmware[323] = 0b1010001000000011010100100000001001
# PC <- PC + 1; fetch; GOTO 290
firmware[324] = 0b0000000001000001010000100000001010
# PC <- MBR; fetch; GOTO MBR;

def read_regs(reg_num):
    global BUS_A, BUS_B, H, MDR, PC, MBR, X, Y, V, S

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
    elif reg_num == 6:
        BUS_B = S
    else:
        BUS_B = 0


def write_regs(reg_bits):
    global MAR, MDR, PC, X, Y, H, V, S, BUS_C

    if reg_bits & 0b10000000:
        MAR = BUS_C
    if reg_bits & 0b01000000:
        MDR = BUS_C
    if reg_bits & 0b00100000:
        PC = BUS_C
    if reg_bits & 0b00010000:
        X = BUS_C
    if reg_bits & 0b00001000:
        Y = BUS_C
    if reg_bits & 0b00000100:
        H = BUS_C
    if reg_bits & 0b00000010:
        V = BUS_C
    if reg_bits & 0b00000001:
        S = BUS_C


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

    read_regs(MIR & 0b0000000000000000000000000000000111)
    alu((MIR & 0b0000000000001111111100000000000000) >> 14)
    write_regs((MIR & 0b0000000000000000000011111111000000) >> 6)
    memory_io((MIR & 0b0000000000000000000000000000111000) >> 3)
    next_instruction((MIR & 0b1111111110000000000000000000000000) >> 25,
                     (MIR & 0b0000000001110000000000000000000000) >> 22)

    return True










