from all_constants import *
from validity_checker import *
from generateBinary import returnBinary
import helpers

# taking in the input from stdin
instructions = []
while True:
    try:
        instructions.append(input())
    except EOFError:
        break

# instructions = [i for i in instructions if i] # removing empty lines

# Other misc constants 
MAX_IMM_VALUE = 2**8 - 1
MAX_NO_OF_INSTRUCTIONS = 2**8

#variables to be used while generating the binary code
mem_addr_vars = {} #format label : instruction_number
variables = [] # variables defined at the start of the program. It will store dictionaries of format name:address
line_counter = 0
Error = False

# main loop
def main():

    for j, inst in enumerate(instructions):
        #if there are more than 256 instructions, throw error
        if j > 255:
            Error = True
            print("Error : Memory overflow")
            return;

        #checking if it's a variable
        isvar, name = helpers.isVar(inst, variables=variables, memory=mem_addr_vars)
        if isvar:
            variables.append({name: 0})
        else:
            if name:
                print(f"Error in line : {name}")
                Error = False
                return
            break
    print(j)
    line_counter = len(instructions) - j
    memory_add = line_counter+1

    #assigning memory address to variables
    for i in variables:
        key = list(i.keys())[0]
        i[key] = memory_add
        memory_add+=1

    #parsing for labels
    for index, inst in enumerate(instructions[j:]):
        if helpers.overflow(index+j):
            print(helpers.overflow(index+j))
            Error = True
            return
        
        # print(inst)
        if (weakIsLabel(inst, variables=variables, memory=mem_addr_vars))[0]:
            inst = inst.split()
            mem_addr_vars[inst[0][:-1]] = index
    # print(variables)
    # print(mem_addr_vars)

    # main loop for generating binary code
    for index, inst in enumerate(instructions[j:]):

        # print(inst)
        validInst, instMessage = isValidInstr(inst, variables=variables, memory=mem_addr_vars)
        validLabel, labelMessage = isValidLabel(inst, variables=variables, memory=mem_addr_vars)
        # print(validInst, validLabel)

        #overflow condition
        if helpers.overflow(index+j):
            print(helpers.overflow(index+j))
            Error = True
            return

        # If there is some variable declaration after all the variables have been declared at the top
        if isVar(inst, variables=variables, memory=mem_addr_vars)[0]:
            print(f"Error found in line {index+j} : Variable definition after all variables have been declared")
            Error = True
            return

        # If instruction is neither a valid label, or a valid instruction
        if (validLabel):
            instToken = inst.split()
            tempInst = " ".join(instToken[1:])
            print(returnBinary(tempInst, variables=variables, memory=mem_addr_vars))

            #making sure last instruction is always hlt
            if helpers.returnType(tempInst) == "f":
                if (index+j+1) != len(instructions):
                    print(f"Error found in line {index+j+1}: Instructions after hlt are invalid\n")
                    Error = True
                    return
            continue
        
        if validInst:
            print(returnBinary(inst, variables=variables, memory=mem_addr_vars))
            if helpers.returnType(tempInst) == "f":
                if (index+j+1) != len(instructions):
                    print(f"Error found in line {index+j+1}: Instructions after hlt are invalid\n")
                    Error = True
                    return
            continue
        
        # If instruction is not a valid instruction
        if (not validLabel):
            if (not validInst):
                print(f"Error found in line {index+j}: {instMessage}")
                Error = True
                return
            else:
                print(f"Error found in line {index+j} : {labelMessage}")
                Error = True
                return
        
        
        # if (not validInst):
        #     pass
        

        # if (validLabel):
        #     pass

main()
    

if Error:
    print("Program did not compile properly\n")