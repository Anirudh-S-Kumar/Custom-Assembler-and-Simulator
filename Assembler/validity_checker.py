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
    return False    


def isVar(inst: str) -> bool:
    inst.split()
    if inst[0] == "var":
        return True
    return False



def ValidityCheckerInstr(inst: str) -> bool:
    """return True if the instruction is a valid instruction, else returns false"""
    
    inst.split()

    if not (isInstruction(inst[0])): # Ignoring labels
        return False

    type = opcode[inst[0]]["type"]
    type_struct = type_structure[type]

