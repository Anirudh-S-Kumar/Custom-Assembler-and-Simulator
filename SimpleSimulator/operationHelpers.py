from simulatorHelpers import *



def typeA(inst: str) -> tuple:
    """Returns tuple of values to be used by all type A instructions
    For type A, will return the tuple (reg1, reg2)
    """
    reg1_value = getRegValue(inst[7:10])
    reg2_value = getRegValue(inst[10:13])

    return (reg1_value, reg2_value)


def typeB(inst: str) -> tuple:
    """Returns tuple of values to be used by all type A instructions
    For type B, will return the tuple (reg1, Immediate values)
    """
    reg1_value = getRegValue(inst[5:8])
    Imm = getDecimal(inst[8:])

    return (reg1_value, Imm)