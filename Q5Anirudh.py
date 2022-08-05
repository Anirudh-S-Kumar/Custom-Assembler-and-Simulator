
print("-----------INITIAL INPUTS-----------")

# space is in bits
space = input("Enter space in memory : ")
space = space.split()
if space[1] == 'Mb':
    space = int(space[0] * (2 ** 6) * 1)
else:
    space = int(space[0] * (2 ** 6) * 2 ** 4)

print("""
1. Bit addressable memory
2. Byte addressable memory
3. Nibble addressable memory
4. Word addressable memory

""")


# word_size stores how the memory is accessed
word_size = 0

address_type = int(input("Enter Address Type (1-4): "))
if (address_type == 1):
    word_size = 1
elif (address_type == 3):
    word_size = 4
else:
    word_size = 8


def ques1() -> None:
    print("\n-----------QUESTION 1-----------\n")
    inst_length = int(input("Enter your Instruction Length: "))
    reg_length = int(input("Enter Register Length: "))

    # no. of bits used to address the memory
    address_bits = space / word_size

    # q is length of opcodes
    q = inst_length - address_bits - reg_length

    # r is filler bits
    r = inst_length - (q + 2*reg_length)

    print(f"""
	Minimum bits needed for representing an address:    	{address_bits}
	Number of bits need by opcode:                  		{q}
	Number of filler bits in Instruction type 2:    		{r}
	Maximum number of instructions this ISA can support: 	{2 ** q}
	Maximum number of registers this ISA can support: 		{2 ** reg_length}
	""")


cont = 'y'
while cont == 'y':
    ques1()
    cont = input("Do you want to repeat Q1 again? [y/n] : ").strip()
