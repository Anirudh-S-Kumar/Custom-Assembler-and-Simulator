from allConstants import *
from assemblerHelpers import returnType, convertToFloatingPoint


def typeA(ins: str) -> str:
    ins = ins.split()
    op = opcodes["type-a"][ins[0]]

    r1 = register_addr[ins[1]]
    r2 = register_addr[ins[2]]
    r3 = register_addr[ins[3]]

    return (op + "00" + r1 + r2 + r3)


def typeB(ins: str) -> str:
    ins = ins.split()
    op = opcodes["type-b"][ins[0]]
    r1 = register_addr[ins[1]]
    imm = '{0:08b}'.format(int(ins[2][1:]))
    return (op+r1+imm)


def typeB(ins: str) -> str:  # modifying type b instruction as immediate value is present here only
    ins = ins.split()
    op = opcodes["type-b"][ins[0]]
    r1 = register_addr[ins[1]]
    imm10 = ins[2][1:]
    if ins[0] == "movf":
        imm = convertToFloatingPoint(float(imm10))
    else:
        imm = '{0:08b}'.format(int(imm10))

    return (op+r1+imm)


def typeC(ins: str) -> str:
    ins = ins.split()
    op = opcodes["type-c"][ins[0]]
    r1 = register_addr[ins[1]]
    r2 = register_addr[ins[2]]
    # since there's no sample test case for this statement so I have not checked
    return (op+"00000"+r1+r2)


def typeD(ins: str, variables: list) -> str:
    ins = ins.split()
    # define a key
    a_key = ins[2]
    address = 0
    for i in variables:
        if a_key in i:
            address = i[a_key]
    mem_addr = '{0:08b}'.format(int(address))
    op = opcodes["type-d"][ins[0]]
    r1 = register_addr[ins[1]]
    #addr = (ins[2])
    return op+r1+mem_addr


# no test cases given in the assignment so, I assume its okay only, check once with edge cases
def typeE(ins: str, memory: dict) -> str:
    ins = ins.split()
    addr = memory[ins[1]]
    mem_addr = '{0:08b}'.format(int(addr))
    op = opcodes["type-e"][ins[0]]
    return op+"000"+mem_addr


def typeF(ins: str) -> str:
    ins = ins.split()
    op = opcodes["type-f"][ins[0]]
    return (op+"00000000000")


def returnBinary(inst: str, variables: list, memory: dict) -> str:
    """Returns the final binary code to be written in the file"""
    type = returnType(inst)
    if type == "a":
        return typeA(inst)
    if type == "b":
        return typeB(inst)
    if type == "c":
        return typeC(inst)
    if type == "d":
        return typeD(inst, variables)
    if type == "e":
        return typeE(inst, memory)
    if type == "f":
        return typeF(inst)


if __name__ == "__main__":
    print(returnBinary("addf R0 R0 R0", [{"xyz": 8, "abc": 9}], {}))
