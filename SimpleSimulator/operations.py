from simulatorHelpers import *
from simulatorConstants import globalTime, time, memoryAddLocation
from operationHelpers import *

# 10110 00 011 001 010

# Make sure to raise flags incase of underflow and overflow
# All functions will return updated program counter
def add(inst: str, pc: int) -> int:
    reg1_value, reg2_value = typeA(inst)
    reg3_value = reg2_value + reg1_value
    overflowFlag(reg3_value)
    setRegValue(reg3_value, inst[13:])
    return pc+1

def sub(inst: str, pc:int) -> int:
    reg1_value, reg2_value = typeA(inst)
    reg3_value = reg2_value - reg1_value
    overflowFlag(reg3_value)
    setRegValue(reg3_value, inst[13:])
    return pc+1

def mov(inst: str, pc:int) -> int:
    reg1_value, ImmVal = typeB(inst)
    setRegValue(ImmVal, inst[5:8])
    return pc+1  # there are two types of mov instructions, type B and type C

def ld(inst: str, pc:int) -> int:
    reg1_value, mem_addr = typeD(inst)
    ldValue = getDecimal(memory[mem_addr])
    setRegValue(ldValue, inst[5:8])

    globalTime.append(time)
    memoryAddLocation(mem_addr)
    time+=1

    return pc+1

def st(inst: str, pc:int) -> int:
    reg1_value, mem_addr = typeD(inst)
    memory[mem_addr] = reg1_value 

    globalTime.append(time)
    memoryAddLocation(mem_addr)
    time+=1

    return pc+1

def mul(inst: str, pc:int) -> int:
    reg1_value, reg2_value = typeA(inst)
    reg3_value = reg2_value * reg1_value
    overflowFlag(reg3_value)
    setRegValue(reg3_value, inst[13:])
    return pc+1

def div(inst: str, pc:int) -> int:
    reg1_value, reg2_value = typeA(inst)
    reg3_value = reg2_value / reg1_value
    overflowFlag(reg3_value)
    setRegValue(reg3_value, inst[13:])
    return pc+1

def rs(inst: str, pc:int) -> int:
    pass

def ls(inst: str, pc:int) -> int:
    pass

def xor(inst: str, pc:int) -> int:
    pass

def or1(inst: str, pc:int) -> int:
    pass

def and1(inst: str, pc:int) -> int:
    pass

def not1(inst: str, pc:int) -> int:
    pass

def cmp(inst: str, pc:int) -> int:
    pass

def jmp(inst: str, pc:int) -> int:
    pass

def jlt(inst: str, pc:int) -> int:
    pass

def jgt(inst: str, pc:int) -> int:
    pass

def je(inst: str, pc:int) -> int:
    pass

def hlt(inst: str, pc:int) -> int:
    return pc+1

def addf(inst: str) -> int:
    pass

def subf(inst: str) -> int:
    pass

def movf(inst: str) -> int:
    pass


mapping = {
    '10000' : add   ,   
    '10001' : sub   ,
    '10110' : mul   ,
    '11010' : xor   ,
    '11011' : or1   ,
    '11100' : and1  ,
    '00000' : addf  ,
    '00001' : subf  ,
    '10010' : mov   ,
    '11000' : rs    ,
    '11001' : ls    ,
    '00010' : movf  ,
    '10011' : mov   ,
    '10111' : div   ,
    '11101' : not1  ,
    '11110' : cmp   ,
    '10100' : ld    ,
    '10101' : st    ,
    '11111' : jmp   ,
    '01100' : jlt   ,
    '01101' : jgt   ,
    '01111' : je    ,
    '01010' : hlt
}


def main():
    # add("1011000011001010")
    pass


if __name__ == "__main__":
    main()
