from all_constants import *

def type_a(ins:str) -> str:
    ins = ins.split()
    op = opcodes["type-a"][ins[0]]
    
    r1 = register_addr[ins[1]]
    r2 = register_addr[ins[2]]
    r3 = register_addr[ins[3]]

    return (op + "00" + r1 + r2 + r3)


    '''def type_b(ins:str) ->str:  #modifying type b instruction as immediate value is present here only
        ins = ins.split()
        op = opcodes["type-b"][ins[0]]
        r1 = register_addr[ins[1]]
        
        imm = '{0:08b}'.format(int(ins[2][1:]))
        return (op+r1+imm)'''
def type_b(ins:str) ->str:  #modifying type b instruction as immediate value is present here only
    ins = ins.split()
    op = opcodes["type-b"][ins[0]]
    r1 = register_addr[ins[1]]
    if ValidInst==True and instMessage == 1:  #validinstr and instmessage is defined in validity checker
        #int(instToken[i][1:]) should go in mov
        imm = '{0:08b}'.format(int(ins[2][1:]))
    if ValidInst==True and instMessage == 0:
        imm = '{0:08b}'.format(float(ins[2][1:]))
    return (op+r1+imm)



def type_c(ins:str) ->str:
    ins = ins.split()
    op = opcodes["type-c"][ins[0]]
    r1 = register_addr[ins[1]]
    r2 = register_addr[ins[2]]
    return (op+"00000"+r1+r2)  #since there's no sample test case for this statement so I have not checked


def type_f(ins:str) ->str:
    ins = ins.split()
    op = opcodes["type-f"][ins[0]]
    return (op+"00000000000")


def type_d(ins:str, memory:dict)->str:
    ins = ins.split()
    addr = memory[ins[2]]
    mem_addr = '{0:08b}'.format(int(addr))
    op = opcodes["type-d"][ins[0]]
    r1 = register_addr[ins[1]]
    #addr = (ins[2])
    return op+r1+mem_addr

def type_e(ins:str, memory:dict)->str:  #no test cases given in the assignment so, I assume its okay only, check once with edge cases
    ins = ins.split()
    addr = memory[ins[2]]
    mem_addr = '{0:08b}'.format(int(addr))
    op = opcodes["type-e"][ins[0]]
    return op+"000"+mem_addr  


def main():
    pass

if __name__ == "__main__":
    main()
    print(type_d("st R3 X",{"X":5}))
