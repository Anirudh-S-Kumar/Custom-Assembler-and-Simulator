from simulator_constants import *
from exec_engine import exec_engine

# initializing program counter
pc = 0
halted = False

# getting binaries from stdin
while True:
    try:
        temp = input()
        memory[pc] = temp
        pc+=1
    except EOFError:
        pc = 0  # resetting pc to 0
        break

def main():
    while not halted:
        inst = memory[pc]
        halted, pc = exec_engine(inst)


if __name__ == "__main__":
    main()