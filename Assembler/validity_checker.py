from all_constants import *
from helpers import *


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