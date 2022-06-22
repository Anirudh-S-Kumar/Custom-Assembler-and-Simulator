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

def isEmpty(inst: str) -> bool:
    if not inst: # ignoring empty lines
        return True    

def ValidityCheckerInstr(inst: str) -> bool:
    """return True if the instruction is a valid instruction, else returns false"""
    #Convert the instruction into 
    
    inst.split()

    if not (isInstruction(inst[0])): # Ignoring labels
        return False

    type = opcode[inst[0]]["type"]
    type_struct = type_structure[type]