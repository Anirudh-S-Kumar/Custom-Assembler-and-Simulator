from simulatorHelpers import *



def typeA(inst: str) -> tuple:
    """Returns tuple of values to be used by all type A instructions
    For type A, will return the tuple (reg1, reg2)
    """
    reg1_value = getRegValue(inst[7:10])
    reg2_value = getRegValue(inst[10:13])

    return (reg1_value, reg2_value)