from simulatorHelpers import *



def typeA(inst: str) -> tuple:
    """Returns tuple of values to be used by all type A instructions
    For type A, will return the tuple (reg1, reg2)
    """
    reg1_value = getRegValue(inst[7:10])
    reg2_value = getRegValue(inst[10:13])

    return (reg1_value, reg2_value)


def typeB(inst: str) -> tuple:
    """Returns tuple of values to be used by all type B instructions
    For type B, will return the tuple (reg1, Immediate values)
    """
    reg1_value = getRegValue(inst[5:8])
    Imm = getDecimal(inst[8:])

    return (reg1_value, Imm)

def typeC(inst: str) -> tuple:
    """Returns tuple of values to be used by all type C instructions
    For type C, will return the tuple (reg1, reg2)
    """
    reg1_value = getRegValue(inst[10:13])
    reg2_value = getRegValue(inst[13:16])

    return (reg1_value, reg2_value)

def typeD(inst: str) -> tuple:
    """Returns tuple of values to be used by all type D instructions
    For type D, will return the tuple (reg1, memory address)
    """
    reg1_value = getRegValue(inst[5:8])
    mem_addr = getDecimal(inst[8:16])

    return (reg1_value, mem_addr)

def typeE(inst: str) -> tuple:
    """Returns tuple of values to be used by all type D instructions
    For type E, will return the tuple (memory address)
    """

    mem_addr = getDecimal(inst[8:16])

    return (mem_addr,)