from math import log2, ceil


space_mapping = {
    'k': 3,
    'm': 6,
    'g': 9,
    't': 12
}


print("-----------INITIAL INPUTS-----------")

# space is in bits
input_space = input("Enter space in memory : ")
input_space = input_space.split()
space = int(input_space[0])

multiplier = (input_space[1][0]).lower()
b_or_B = input_space[1][1]

if multiplier != 'b':
    space = space * (2 ** space_mapping[multiplier])

if b_or_B == 'B':
    space = space * 2 ** 3


def get_word_size(CPU: int = 0) -> int:
    """
    Returns the size of the words used. 
    """
    print("1. Bit Addressable Memory - Cell Size = 1 bit")
    print("2. Nibble Addressable Memory - Cell Size = 4 bit")
    print("3. Byte Addressable Memory - Cell Size = 8 bits(standard)")
    print("4. Word Addressable Memory - Cell Size = Word Size (depends on CPU)")

    # word_size stores how the memory is accessed
    word_size = 0

    address_type = int(input("Enter Address Type (1-4): "))
    if (address_type == 1):
        word_size = 1
    elif (address_type == 2):
        word_size = 4
    elif (address_type == 8 and CPU != 0):
        word_size = CPU
    else:
        word_size = 8

    return word_size


word_size = get_word_size()


# Question 1
def ques1() -> None:
    global space
    global word_size

    print("\n-----------QUESTION 1-----------\n")
    inst_length = int(input("Enter your Instruction Length: "))
    reg_length = int(input("Enter Register Length: "))
    # no. of bits used to address the memory
    address_bits = ceil(log2(space / word_size))

    # q is length of opcodes
    q = inst_length - address_bits - reg_length

    # r is filler bits
    r = inst_length - (q + 2*reg_length)

    print("-----------ANSWER 1-----------")
    print(f"Minimum bits needed for representing an address: {address_bits}")
    print(f"Number of bits need by opcode: {q}")
    print(f"Number of filler bits in Instruction type 2: {r}")
    print(f"Maximum number of instructions this ISA can support: {2 ** q}")
    print(
        f"Maximum number of registers this ISA can support: {2 ** reg_length}")


cont = 'y'
while cont == 'y':
    ques1()
    cont = (input("Do you want to repeat Q1 again? [y/n] : ").strip()).lower()


def ques2() -> None:
    global space
    global word_size

    print("\n-----------QUESTION 2-----------\n")

    query = int(input("Enter type of query[1/2] : ").strip())

    # Number of bits in CPU
    bitCPU = int(input("Enter the number bits in CPU: "))
    bitCPU = bitCPU.split()

    if query == 1:
        new_word_size = get_word_size(CPU=bitCPU)

        old_address_bits = ceil(log2(space / word_size))
        new_address_bits = ceil(log2(space / new_word_size))
        delta = old_address_bits - new_address_bits

        if (delta >= 0):
            print("+", end='')
        print(delta)
    else:
        # Number of address pins
        address_pins = int(input("Enter the number of address pins: "))

        # word size
        new_word_size = get_word_size(CPU=bitCPU)

        # memory size in bits
        memory_size = new_word_size * (2 ** (address_pins))

        memory_size = memory_size/8  # conversion to bytes
        memory_size = memory_size/1024  # conversion to KB
        memory_size = memory_size/1024  # conversion to MB
        memory_size = memory_size/1024  # conversion to GB

        print(f"{memory_size} GB")
