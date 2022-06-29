from all_constants import *
from validity_checker import *
import helpers

# taking in the input from file
instructions = []
with open("dummy.txt", "r") as f:
    instructions = f.read().splitlines()

instructions = [i for i in instructions if i] # removing empty lines


# creating the output file for the binary
fout = open("output.txt", "w")

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
            fout.write("Error : Memory overflow")
            Error = True
            return;

        #checking if it's a variable
        isvar, name = helpers.isVar(inst, variables, mem_addr_vars)
        if isvar:
            variables.append({name: 0})
        else:
            if name:
                fout.write(f"Error in line : {name}")
                fout.write('\n')
                Error = False
                return
            break

    line_counter = len(instructions) - j
    memory_add = line_counter+1

    #assigning memory address to variables
    for i in variables:
        key = list(i.keys())[0]
        i[key] = memory_add
        memory_add+=1


    # main loop for generating binary code
    for index, inst in enumerate(instructions[j:]):
        validInst, instMessage = isValidInstr(inst, variables=variables, memory=mem_addr_vars)
        validLabel, labelMessage = isValidLabel(inst, variables=variables, memory=mem_addr_vars)

        if (index+j) > 255:
            fout.write("Error : Memory overflow")
            Error = True
            return

        # If there is some variable declaration after all the variables have been declared at the top
        if isVar(inst)[0]:
            fout.write(f"Error found in line {index} : Variable definition after all variables have been declared")
            Error = True
            return

        # If instruction is neither a valid label, or a valid instruction
        if (not validLabel):
            fout.write(f"Error found in line {index}: {labelMessage}")
            Error = True
            return
        
        # If instruction is not a valid instruction
        if (not validInst):
            fout.write(f"Error found in line {index} : {instMessage}")
            Error = True
            return
        

        if (validLabel):
            pass


    

if Error:
    fout.write("Program did not compile properly\n")
else:
    pass