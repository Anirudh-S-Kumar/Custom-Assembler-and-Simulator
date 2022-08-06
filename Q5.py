from math import log2, ceil
import platform


space_mapping = {
    'k': 10,
    'm': 20,
    'g': 30,
    't': 40
}

# Assuming word size to be the same as the one the program is being run on
words = {
    'b': 1,
    'Nib': 4,
    'B': 8,
    'Word': platform.architecture()[0][0:2]
}

print("-----------INITIAL INPUTS-----------")

# space is in bits
input_space = input("Enter space in memory : ")
input_space = input_space.split()
space = int(input_space[0])

# no multiplier is set to true if there is no multiplier in front of word size
no_multiplier = False
multiplier = (input_space[1][0]).lower()
rest = input_space[1][1:]


if rest == 'Word':
    bitCPU = int(input("Enter the number bits in CPU: "))
    words['Word'] = bitCPU


if multiplier in space_mapping:
    space = space * (2 ** space_mapping[multiplier])
else:
    no_multiplier = True


# changing value of rest incase there is no multiplier
if no_multiplier:
    rest = input_space[1]

if rest in words:
    space = space * words[rest]


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
    elif (address_type == 4 and CPU != 0):
        word_size = CPU
    else:
        word_size = 8

    return word_size


word_size = get_word_size(bitCPU)


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

    print()
    print(f"Minimum bits needed for representing an address: {address_bits}")
    print(f"Number of bits need by opcode: {q}")
    print(f"Number of filler bits in Instruction type 2: {r}")
    print(f"Maximum number of instructions this ISA can support: {2 ** q}")
    print(
        f"Maximum number of registers this ISA can support: {2 ** reg_length}")


print("\n-----------QUERIES-----------")
print()
cont = (input("Do you want to do Q1? [y/n] : ").strip()).lower()
while cont == 'y':
    ques1()
    cont = (input("Do you want to repeat Q1 again? [y/n] : ").strip()).lower()


def ques2() -> None:
    global space
    global word_size

    print("\n-----------QUESTION 2-----------\n")

    print("1. Changing addressable memory")
    print("2. Memory size")

    query = int(input("Enter type of query[1/2] : ").strip())

    # Number of bits in CPU
    bitCPU = int(input("Enter the number bits in CPU: "))

    if query == 1:
        new_word_size = get_word_size(CPU=bitCPU)
        old_address_bits = ceil(log2(space / word_size))
        new_address_bits = ceil(log2(space / new_word_size))
        delta = new_address_bits - old_address_bits

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
        i = 0
        while(memory_size / (2 ** (10 * i)) > 1):
            i += 1
        i -= 1
        print(i)
        memory_size = memory_size / 2 ** (10 * i)
        if i == 0:
            print(f"{memory_size} B")
        elif i == 1:
            print(f"{memory_size} KB")
        elif i == 2:
            print(f"{memory_size} MB")
        elif i == 3:
            print(f"{memory_size} GB")
        else:
            print(f"{memory_size} TB")


print()
cont = (input("Do you want to do Q2? [y/n] : ").strip()).lower()
while cont == 'y':
    ques2()
    cont = (input("Do you want to repeat Q2 again? [y/n] : ").strip()).lower()
