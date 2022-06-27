from all_constants import *


def isInstruction(val: str) -> bool:
    for i in opcodes:
        if val in opcodes[i]:
            return True
    return False 


def isRegister(val: str) -> bool:
    if val in register_addr:
        return True
    return False

def isVar(inst: str) -> tuple:
    inst.split()
    if inst[0] == "var":
        if len(inst) == 2:
            return True, inst[1]
        return False, "Illegal definition of variable"
    return False, ""



def inVars(var:str, variables:list) -> bool:
    """Returns True if given variable is in the list of variables or not"""
    for i in variables:
        if var in i:
            return True
    return False

def inMemory(addr:str, memory:dict):
    """Returns True if given variable is in the list of variables or not"""
    if addr in memory:
        return True
    return False


def isValidName(var:str, variables:list, memory:dict) -> bool:
    """Returns True if the variable name is valid, and False otherwise"""
    if inVars(vars) or inMemory(var, memory=memory) or isInstruction(var):
        return False
    return True
