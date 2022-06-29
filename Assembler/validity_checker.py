from all_constants import *
from helpers import *


def isValidInstr(inst: str, variables: list, memory:dict) -> tuple:
    """Return True if the instruction is a valid instruction, else returns false
    
    Parameter
    -------
    inst : str
        The instruction to be evaluated
    variables : list
        list of variables that have been added already
    memory : dict
        list of labels defined in the program
    """
    
    inst = inst.split()
    validIns = isInstruction(inst[0])
    if not (validIns): # Returning false if Instruction is not a valid instruction
        return False, "Instruction given is not a valid instruction"

    type = returnType(inst)

    type_struct = type_structure[type]

    #iterating through all the elements of the instruction and making sure all are correct
    i = 0
    for j in type_struct:
        # try:
            if j == "unused":
                continue

            if j == "opcode":
                i+=1    
                continue

            elif j == "memory":
                if type == 'd':
                    if not inVars(inst[i], variables):
                        return False , f"'{inst[i]}' variable not defined"
                elif type == "e":
                    if not inMemory(inst[i], memory):
                        return False, f"'{inst[i]}' label used is not defined"


            elif j == "immediate":
                if inst[i][0] != "$":
                    return False, "Immediate value missing"

            elif j == "reg":
                if not isRegister(inst[i]):
                    return False, f"'{inst[i]}'is not a Valid Register"
            i+=1
        # except:
        #     return False, "Something went terribly wrong. Should check up on that"

    return True, "" # returning true with an empty string if all checks pass

def weakIsLabel(inst:str, variables:list, memory:dict) -> tuple:
    """A weaker version of the isValidLabel instruction"""
    inst.split()
    if (inst[0][-1] != ":"):
        return False, "Colon missing after label"

    validName = isValidName(inst[0][:-1], variables, memory=memory)
    if not validName:
        return False, "Label name cannot be an instruction, an already existing variable name or memory address"


def isValidLabel(inst: str, variables: list, memory: dict) -> tuple:
    """Returns True if it's a valid label, and returns false otherwise
    Also returns an empty string if it's a label, and error message otherwise
    Parameter
    -------
    inst : str
        The instruction to be evaluated
    variables : list
        list of variables that have been added already
    memory : dict
        list of labels defined in the program
    """

    validName, message = weakIsLabel(inst, variables=variables, memory=memory)
    if not validName:
        return validName, message

    temp1, temp2 = isValidInstr(inst[1:], variables=variables, memory=memory)
    return temp1, temp2

# def notValid(inst:str, variables:list, memory:str) -> bool:
#     """Return true if an instruction is valid at all or not"""
#     pass

def main():
    """For Testing only"""
    variables = [{"abc": 10, "asdwe": 11, "asdawd":12}]
    memory = {"sub1":5, "sub2": 7}
    print(isValidInstr("cmp R1 R0 ", variables=variables, memory=memory))


if __name__ == "__main__":
    main()