from all_constants import *

# Helpers

def isInstruction(val: str) -> tuple:
    for i in opcodes:
        if val in opcodes[i]:
            return True, i
    return False, "Instruction given is not a valid instruction"


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



def isValidInstr(inst: str, vars: dict) -> tuple:
    """Return True if the instruction is a valid instruction, else returns false
    
    Parameter
    -------
    inst : str
        The instruction to be evaluated
    vars : dict
        list of variables that have been added already
    """
    
    inst.split()
    validIns, returnString = isInstruction(inst[0])

    if not (validIns): # Returning false if Instruction is not a valid instruction
        return False, returnString

    type = returnString
    type_struct = type_structure[type]

    #iterating through all the elements of the instruction and making sure all are correct
    for j, i in enumerate(inst):
        if type_struct[j] == "unused":
            continue

        if type_struct[j] == "opcode":
            continue

        elif type_struct[j] == "memory":
            if i not in vars:
                return False , "Memory address not defined"

        elif type_struct[j] == "immediate":
            if i[0] != "$":
                return False, "Immediate value missing"

        elif type_struct[j] == "reg":
            if not isRegister(i):
                return False, "Not a Valid Register"

    return True, "" # returning true with an empty string if all checks pass

def isValidLabel(inst: str, vars: dict) -> tuple:
    pass