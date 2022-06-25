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



def isValidInstr(inst: str, vars: dict) -> bool:
    """Return True if the instruction is a valid instruction, else returns false
    
    Parameter
    -------
    inst : str
        The instruction to be evaluated
    vars : dict
        list of variables that have been added already
    """
    
    inst.split()

    if not (isInstruction(inst[0])): # Ignoring labels
        return False

    type = opcode[inst[0]]["type"]
    type_struct = type_structure[type]

    #interating through all the elements of the instruction and making sure all are correct
    for j, i in enumerate(inst):
        if type_struct[j] == "unused":
            continue
        if type_struct[j] == "opcode":
            if not isInstruction(i):
                raise NameError("Instruction not in the ISA specification")

        elif type_struct[j] == "memory":
            if i not in vars:
                raise NameError("Memory address not defined")

        elif type_struct[j] == "immediate":
            if i[0] != "$":
                raise NameError("Immediate value missing")

