from simulatorConstants import *
from simulatorHelpers import dumpRegs, base2Bit8, memoryDump
from execEngine import executionEngine

# initializing program counter
pc = 0

# getting binaries from stdin
while True:
    try:
        temp = input()
        memory[pc] = temp
        pc+=1
    except EOFError:
        break

def main():
    halted = False
    pc = 0
    while not halted:
        inst = memory[pc]
        pcBase2 = base2Bit8(pc)
        print(pcBase2, end = " ")
        halted, pc = executionEngine(inst, pc)
        dumpRegs()
    # memoryDump()

# if __name__ == "__main__":
main()