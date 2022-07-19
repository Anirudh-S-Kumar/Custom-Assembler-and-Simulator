import operations
from simulatorHelpers import getRegValue


def executionEngine(inst: str, pc:int) -> tuple:
    """
    Will perform all the computations necessary for the given instructions, and return a tuple
    First value will be if the program has to be halted or not
    Second value will be new value of program counter
    """
    halted = False
    opcode = inst[:5]
    newPC = tuple(map(operations.mapping[opcode], [inst], [pc]))[0]

    if opcode == "01010":
        halted = True
    return (halted, newPC)


def main():
    # executionEngine("")
    pass

if __name__ == "__main__":
    main()