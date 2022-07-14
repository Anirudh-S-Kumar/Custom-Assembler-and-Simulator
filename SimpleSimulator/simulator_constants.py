import sys, os

abs_path = os.path.split(os.getcwd())[0] + "/CO_Project/" 
sys.path.append(abs_path + "/Simple-Assembler")

from all_constants import register_addr, opcodes

# making a dictionary of dictionaries
# initializing all values to 0 at the beginning
register = {}

for i in register_addr:
    register[register_addr[i]] = {i : 0}
