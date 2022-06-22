from all_constants import *

# Helpers

def isInstruction(val: str) -> bool:
    if val in opcode:
        return True
    return False

def isRegister(val: str) -> bool:
    if val in register_addr:
        return True
    return False

def ValidityChecker(inst: str) -> bool:
    """return True if the instruction is a valid instruction, else returns false"""
    #Convert the instruction into 
    if not inst: # ignoring empty lines
        return True
    
    inst.split()