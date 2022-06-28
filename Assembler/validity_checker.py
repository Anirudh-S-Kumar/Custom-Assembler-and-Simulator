from all_constants import *
from helpers import *


def isValidInstr(inst: str, variables: list, memory:dict) -> tuple:
    """Return True if the instruction is a valid instruction, else returns false
    
    Parameter
    -------
    inst : str
        The instruction to be evaluated
    vars : list
        list of variables that have been added already
    memory : dict
        list of labels defined in the program
    """
    
    inst.split()
    validIns = isInstruction(inst[0])

    if not (validIns): # Returning false if Instruction is not a valid instruction
        return False, "Instruction given is not a valid instruction"

    type = returnType(inst)

    type_struct = type_structure[type]

    #iterating through all the elements of the instruction and making sure all are correct
    i = 0
    for j in type_struct:
        try:
            if j == "unused":
                continue

            if type_struct[j] == "opcode":
                i+=1
                continue

            elif type_struct[j] == "memory":
                if type == 'd':
                    if not inVars(inst[i], vars):
                        return False , "Variable not defined"
                elif type == "e":
                    if not inMemory():
                        return False, "Label used is not defined"


            elif type_struct[j] == "immediate":
                if inst[i][0] != "$":
                    return False, "Immediate value missing"

            elif type_struct[j] == "reg":
                if not isRegister(inst[i]):
                    return False, "Not a Valid Register"
            i+=1
        except:
            return False, "Something went terribly wrong. Should check up on that"

    return True, "" # returning true with an empty string if all checks pass

def isValidLabel(inst: str, variables: list, memory: dict) -> tuple:
    """Returns True if it's a valid label, and returns false otherwise
    Also returns an empty string if it's a label, and error message otherwise
    Parameter
    -------
    inst : str
        The instruction to be evaluated
    vars : list
        list of variables that have been added already
    memory : dict
        list of labels defined in the program
    """
    inst.split()
    if (inst[0][-1] != ":"):
        return False, "Colon missing after label"

    validName = isValidName(inst[0][:-1], vars, memory=memory)
    if not validName:
        return False, "Label name cannot be an instruction, an already existing variable name or memory address"

    temp1, temp2 = isValidInstr(inst[1:], variables=variables, memory=memory)
    return temp1, temp2
def main():
    """For Testing only"""
    variables = []
    isValidInstr()


if __name__ == "__main__":
    main()