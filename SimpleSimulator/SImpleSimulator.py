from simulatorConstants import *
from simulatorHelpers import dumpRegs, base2Bit8, memoryDump
from execEngine import executionEngine
import matplotlib.pyplot as plot

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
    time = 0
    while not halted:
        globalTime.append(time)
        memoryAddLocation.append(pc)
        time+=1
        inst = memory[pc]
        pcBase2 = base2Bit8(pc)
        print(pcBase2, end = " ")
        halted, pc = executionEngine(inst, pc)
        dumpRegs()
    
    memoryDump()
    plot.scatter(x=globalTime, y=memoryAddLocation)
    plot.title("Memory location access scatter plot")
    plot.xlabel('Time')
    plot.ylabel('Memory Location')
    plot.show()


main()


