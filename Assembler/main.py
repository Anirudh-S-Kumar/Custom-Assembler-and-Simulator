from all_constants import *
from validity_checker import *

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
for j, i in enumerate(instructions):

    #checking if it's a variable
    isvar, name = isVar(i)
    if isvar:
        variables.append({name: 0})
    else:
        if name:
            fout.write(name)
            fout.write('\n')
            Error = False
            break
        break

line_counter = len(instructions) - j


if Error:
    fout.write("Program did not compile properly\n")
else:
    fout.write("Programmed Compiled properly\n")