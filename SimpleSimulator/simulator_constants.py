import sys, os

abs_path = os.path.split(os.getcwd())[0] + "/CO_Project/" 
sys.path.append(abs_path + "/Simple-Assembler")

from all_constants import register_addr, opcodes

# making a dictionary of dictionaries
# initializing all values to 0 at the beginning
register = {}

for i in register_addr:
    register[register_addr[i]] = {i : 0}

# initializing memory
memory = []

for i in range(256):
    memory.append("0" * 16)

if __name__ == "__main__":
    print(*memory)