import operations
from simulatorHelpers import getRegValue






def execEngine(inst: str, pc:int) -> tuple:
    """
    Will perform all the computations necessary for the given instructions, and return a tuple
    First value will be if the program has to be halted or not
    Second value will be new value of program counter
    """
    opcode = inst[:5]
    a1 = tuple(map(operations.mapping[opcode], [inst], [pc]))
    print(a1)
    


def main():
    execEngine("")

if __name__ == "__main__":
    main()