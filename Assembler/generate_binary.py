from all_constants import *

def type_a(ins):
    op = opcodes["type-a"][ins[0]]
    
    r1 = register_addr[ins[1]]
    r2 = register_addr[ins[2]]
    r3 = register_addr[ins[3]]

    return (op + "00" + r1 + r2 + r3)

def type_b(ins):
    op = opcodes["type-b"][ins[0]]
    r1 = register_addr[ins[1]]
    imm = '{0:08b}'.format(int(ins[2][1:]))
    return (op+r1+imm)


