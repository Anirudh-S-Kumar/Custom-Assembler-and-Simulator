from allConstants import *
from math import log2, floor


def getFractional(num: float) -> float:
    """Return fractional part of num"""
    return num-int(num)


def exponentCount(num: float) -> int:
    return len(str(num).split(".")[1])


def validFloat(num: float) -> bool:
    if not validRange(num):
        return False

    val = num / 2**floor(log2((num)))
    exponent = exponentCount(val)
    val = getFractional(val)*(10**exponent)

    if (val % (5**exponent) == 0) and exponent <= 5:
        return True
    else:
        return False


def validRange(num: float) -> bool:
    if 1 <= num <= 252:
        return True
    else:
        return False


def isNumber(num: str) -> bool:
    """
    Takes a string and checks if it's a number (Integer or Float).

    """
    try:
        # only integers and float converts safely
        num = float(num)
        return True
    except ValueError as e:  # not convertible to float
        return False


def convertToFloatingPoint(num: float) -> str:
    """Returns the floating point representation of num"""
    exponent = floor(log2(num))
    fractional10 = (num / 2**exponent) - 1
    fractional2 = ""
    for i in range(5):
        fractional10 *= 2
        f_bit = (int(fractional10))
        fractional10 -= f_bit
        fractional2 += str(f_bit)

    return '{0:03b}'.format(exponent) + fractional2


def isValidChars(val: str) -> bool:
    "Returns True if all the characters in the string are a subset of valid characters"
    val = set(val)
    if validChars.union(val) == validChars:
        return True
    return False


def isInstruction(val: str) -> bool:
    for i in opcodes:
        if val in opcodes[i]:
            return True
    return False


def isImmediate(val: str) -> bool:
    if (val[0] == "$"):
        return True
    return False


def returnType(inst: str) -> str:
    inst = inst.split()
    for i in opcodes:
        if inst[0] in opcodes[i]:
            if (inst[0] == "mov"):
                if isImmediate(inst[-1]):
                    return 'b'
                else:
                    return 'c'
            return i[-1]
    return ""


def isRegister(val: str) -> bool:
    if val in register_addr:
        return True
    return False


def isVar(inst: str, variables: list, memory: dict) -> tuple:
    inst = inst.split()
    if inst[0] == "var":
        if len(inst) == 2:
            if isValidName(inst[1], variables, memory):
                return True, inst[1]
        return False, "Illegal definition of variable"
    return False, ""


def inVars(var: str, variables: list) -> bool:
    """Returns True if given variable is in the list of variables or not"""
    for i in variables:
        if var in i:
            return True
    return False


def inMemory(addr: str, memory: dict):
    """Returns True if given address is in the list of addresses or not"""
    if addr in memory:
        return True
    return False


def isValidName(var: str, variables: list, memory: dict) -> bool:
    """Returns True if the variable name is valid, and False otherwise"""
    if inVars(vars, variables) or inMemory(var, memory=memory) or isInstruction(var) or isRegister(var) or not(isValidChars(var)) or not(var):
        return False
    return True


def overflow(index: int) -> str:
    """Return True if memory overflow has occurred"""
    if (index) > MAX_NO_OF_INSTRUCTIONS:
        return "Error : Memory overflow"
    return ""


if __name__ == "__main__":
    print(validFloat(252))
