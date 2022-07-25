import operations
from simulatorHelpers import resetFlags
from simulatorConstants import rFlag

def executionEngine(inst: str, pc:int) -> tuple:
    """
    Will perform all the computations necessary for the given instructions, and return a tuple
    First value will be if the program has to be halted or not
    Second value will be new value of program counter
    """
    rFlag = True
    halted = False
    opcode = inst[:5]
    newPC, rFlag = tuple(map(operations.mapping[opcode], [inst], [pc]))[0]
    # print(newPC, rFlag)
    if rFlag:
        # print("Flag being reset")
        resetFlags()
    else:
        rFlag = True

    if opcode == "01010":
        halted = True
    return (halted, newPC)


def main():
    # executionEngine("")
    pass

if __name__ == "__main__":
    main()