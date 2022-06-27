from all_constants import *

# Helpers

def isInstruction(val: str) -> bool:
    for i in opcodes:
        if val in opcodes[i]:
            return True
    return False 


def isRegister(val: str) -> bool:
    if val in register_addr:
        return True
    return False

def isValidName(var:str, variables:list, memory:dict) -> bool:
    """Returns True if the variable name is valid, and False otherwise"""
    if inVars(vars) or  


def isVar(inst: str) -> tuple:
    inst.split()
    if inst[0] == "var":
        if len(inst) == 2:
            return True, inst[1]
        return False, "Illegal definition of variable"
    return False, ""

def inMemory():
    pass



def inVars(var:str, variables:list) -> bool:
    """Returns True if given variable is in the list of variables or not"""
    for i in variables:
        if var in i:
            return True
    return False


def isValidInstr(inst: str, vars: list, memory:dict) -> tuple:
    """Return True if the instruction is a valid instruction, else returns false
    
    Parameter
    -------
    inst : str
        The instruction to be evaluated
    vars : dict
        list of variables that have been added already
    memory : dict
        list of labels defined in the program
    """
    
    inst.split()
    validIns = isInstruction(inst[0])

    if not (validIns): # Returning false if Instruction is not a valid instruction
        return False, "Instruction given is not a valid instruction"

    for i in opcodes:
        if inst[0] in opcodes[i]:
            type=opcodes[i][-1]

    type_struct = type_structure[type]

    #iterating through all the elements of the instruction and making sure all are correct
    for j, i in enumerate(inst):
        try:
            if type_struct[j] == "unused":
                continue

            if type_struct[j] == "opcode":
                continue

            elif type_struct[j] == "memory":
                if type=='d':
                    if not inVars(i, vars):
                        return False , "Variable not defined"
                elif type=="e":
                    if i not in memory:
                        return False, "Label used is not defined"


            elif type_struct[j] == "immediate":
                if i[0] != "$":
                    return False, "Immediate value missing"

            elif type_struct[j] == "reg":
                if not isRegister(i):
                    return False, "Not a Valid Register"
        except:
            return False, "Something went terribly wrong. Should check up on that"

    return True, "" # returning true with an empty string if all checks pass

def isValidLabel(inst: str, vars: dict, memory: dict) -> tuple:
    """Returns True if it's a valid label, and returns false otherwise
    Also returns an empty string if it's a label, and error message otherwise
    Parameter
    -------
    inst : str
        The instruction to be evaluated
    vars : dict
        list of variables that have been added already
    memory : dict
        list of labels defined in the program
    """
    inst.split()
    if (inst[0][-1] != ":"):
        return False, "Colon missing after label"

    validIns, returnString = isInstruction[inst[0][:-1:]]

    if validIns:
        return False, "Label name cannot be an instruction"

def main():
    """For Testing only"""


if __name__ == "__main__":
    main()