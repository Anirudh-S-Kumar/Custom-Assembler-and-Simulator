from simulatorHelpers import *
from operationHelpers import *

# 10110 00 011 001 010

# Make sure to raise flags incase of underflow and overflow
def add(inst: str) -> None:
    reg1_value, reg2_value = typeA(inst)
    reg3_value = reg2_value + reg1_value
    overflowFlag(reg3_value)
    setRegValue(reg3_value, inst[13:])


def sub(inst: str) -> None:
    pass

def mov(inst: str) -> None:
    pass

def ld(inst: str) -> None:
    pass

def st(inst: str) -> None:
    pass

def mul(inst: str) -> None:
    pass

def div(inst: str) -> None:
    pass

def rs(inst: str) -> None:
    pass

def ls(inst: str) -> None:
    pass

def xor(inst: str) -> None:
    pass

def or1(inst: str) -> None:
    pass

def and1(inst: str) -> None:
    pass

def not1(inst: str) -> None:
    pass

def cmp(inst: str) -> None:
    pass

def jmp(inst: str) -> None:
    pass

def jlt(inst: str) -> None:
    pass

def jgt(inst: str) -> None:
    pass

def je(inst: str) -> None:
    pass

def hlt(inst: str) -> None:
    pass

def addf(inst: str) -> None:
    pass

def subf(inst: str) -> None:
    pass

def movf(inst: str) -> None:
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