import sys, os

abs_path = os.path.split(os.getcwd())[0]
sys.path.append(abs_path + "/Simple-Assembler")

from allConstants import register_addr, opcodes

# making a dictionary of dictionaries
# initializing all values to 0 at the beginning
register = {}

for i in register_addr:
    register[register_addr[i]] = {i : 0}

# initializing memory
memory = []

for i in range(256):
    memory.append("0" * 16)

# mapping from opcodes to instructions
opcodesToInst = {}

for i in opcodes:
    temp = opcodes[i]
    for j in temp:
        opcodesToInst[temp[j]] = j

memoryAddLocation = [] # stores the corresponding location of memory being accessed at given time
globalTime = []    # stores time intervals to be plotted
time = 0
rFlag = True # 


if __name__ == "__main__":
    # print(*memory)
    for i in register:
        print(i, register[i])