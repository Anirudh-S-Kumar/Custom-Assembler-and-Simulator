from datetime import datetime
from simulatorConstants import *
from simulatorHelpers import dumpRegs, base2Bit8, memoryDump
from execEngine import executionEngine
import matplotlib.pyplot as plot
import cProfile
import pstats
import sys

profiler = cProfile.Profile()


# initializing program counter
pc = 0

# getting binaries from stdin
while True:
    try:
        temp = input()
        temp.rstrip("\n")
        if temp:
            memory[pc] = temp
            pc += 1
    except EOFError:
        break


def main():
    final_output = []
    halted = False
    pc = 0
    time = 0
    while not halted:
        globalTime.append(time)
        memoryAddLocation.append(pc)
        time += 1
        inst = memory[pc]
        pcBase2 = base2Bit8(pc)
        halted, pc = executionEngine(inst, pc)
        dumpRegs()
        temp_final = (" ".join([pcBase2, dumpRegs()]))
        final_output.append(temp_final)

        if len(final_output) > 60:
            sys.stdout.write("\n".join(final_output) + "\n")
            final_output.clear()

    final_output.append(memoryDump())
    sys.stdout.write("\n".join(final_output) + "\n")

    file_name = str(datetime.now())
    plot.scatter(x=globalTime, y=memoryAddLocation)
    plot.title("Memory location access scatter plot")
    plot.xlabel('Time')
    plot.ylabel('Memory Location')
    plot.savefig(f"images/{file_name}.png")


main()
