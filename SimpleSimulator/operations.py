from simulatorHelpers import *
from simulatorConstants import globalTime, time, memoryAddLocation
from operationHelpers import *

# 10110 00 011 001 010

# Make sure to raise flags incase of underflow and overflow
# All functions will return updated program counter
# along with bool value, which determines if rFlags is to be reset or not


def add(inst: str, pc: int) -> tuple:
    reg1_value, reg2_value = typeA(inst)
    reg3_value = reg2_value + reg1_value

    if overflowFlag(reg3_value):
        reg3_value = reg3_value % (2**16)
        setRegValue(reg3_value, inst[13:])
        return pc+1, False

    setRegValue(reg3_value, inst[13:])
    return pc+1, True


def sub(inst: str, pc: int) -> tuple:
    reg1_value, reg2_value = typeA(inst)
    reg3_value = reg1_value - reg2_value

    if overflowFlag(reg3_value):
        setRegValue(0, inst[13:])
        return pc+1, False

    setRegValue(reg3_value, inst[13:])
    return pc+1, True


def mov(inst: str, pc: int) -> tuple:
    reg1_value, ImmVal = typeB(inst)
    setRegValue(ImmVal, inst[5:8])
    return pc+1, True  # there are two types of mov instructions, type B and type C


def movr(inst: str, pc: int) -> tuple:
    reg1_value, reg2_value = typeC(inst)
    setRegValue(reg1_value, inst[13:])
    return pc+1, True


def ld(inst: str, pc: int) -> tuple:
    reg1_value, mem_addr = typeD(inst)
    ldValue = getDecimal(memory[mem_addr])
    print(ldValue)
    setRegValue(ldValue, inst[5:8])

    globalTime.append(globalTime[-1])
    memoryAddLocation.append(mem_addr)

    return pc+1, True


def st(inst: str, pc: int) -> tuple:
    reg1_value, mem_addr = typeD(inst)
    memory[mem_addr] = base2Bit16(reg1_value)

    globalTime.append(globalTime[-1])
    memoryAddLocation.append(mem_addr)

    return pc+1, True


def mul(inst: str, pc: int) -> tuple:
    reg1_value, reg2_value = typeA(inst)
    reg3_value = reg2_value * reg1_value

    if overflowFlag(reg3_value):
        reg3_value = reg3_value % (2**16)
        setRegValue(reg3_value, inst[13:])
        return pc+1, False

    setRegValue(reg3_value, inst[13:])
    return pc+1, True


def div(inst: str, pc: int) -> tuple:
    reg3_value, reg4_value = typeC(inst)
    reg0_value = reg3_value // reg4_value
    reg1_value = reg3_value % reg4_value

    setRegValue(reg0_value, '000')
    setRegValue(reg1_value, '001')

    return pc+1, True


def rs(inst: str, pc: int) -> tuple:
    reg1_value, ImmVal = typeB(inst)
    reg1_value = reg1_value >> ImmVal
    setRegValue(reg1_value, inst[5:8])
    return pc+1, True


def ls(inst: str, pc: int) -> tuple:
    reg1_value, ImmVal = typeB(inst)
    reg1_value = reg1_value << ImmVal
    setRegValue(reg1_value, inst[5:8])
    return pc+1, True


def xor(inst: str, pc: int) -> tuple:
    reg1_value, reg2_value = typeA(inst)
    reg3_value = reg2_value ^ reg1_value
    setRegValue(reg3_value, inst[13:])
    return pc+1, True


def or1(inst: str, pc: int) -> tuple:
    reg1_value, reg2_value = typeA(inst)
    reg3_value = reg2_value | reg1_value
    setRegValue(reg3_value, inst[13:])
    return pc+1, True


def and1(inst: str, pc: int) -> tuple:
    reg1_value, reg2_value = typeA(inst)
    reg3_value = reg2_value & reg1_value
    setRegValue(reg3_value, inst[13:])
    return pc+1, True


def not1(inst: str, pc: int) -> tuple:
    reg1_value, reg2_value = typeC(inst)
    reg2_value = 2**16 - 1 - reg1_value
    setRegValue(reg2_value, inst[13:])
    return pc+1, True


def cmp(inst: str, pc: int) -> tuple:
    global rFlag
    reg1_value, reg2_value = typeC(inst)
    comparisonFlag(reg1_value, reg2_value)
    return pc+1, False


def jmp(inst: str, pc: int) -> tuple:
    reg1_value = typeE(inst)  # taken the decimal value of memory address
    return reg1_value, True


def jlt(inst: str, pc: int) -> tuple:
    mem_location = typeE(inst)
    flag_base2 = base2Bit8(getRegValue("111"))
    if flag_base2[-3] == '1':
        return mem_location, True

    return pc + 1, True


def jgt(inst: str, pc: int) -> tuple:
    mem_location = typeE(inst)
    flag_base2 = base2Bit8(getRegValue("111"))
    if flag_base2[-2] == '1':
        return mem_location, True

    return pc + 1, True


def je(inst: str, pc: int) -> tuple:
    mem_location = typeE(inst)
    flag_base2 = base2Bit8(getRegValue("111"))
    if flag_base2[-1] == '1':
        return mem_location, True

    return pc + 1, True


def hlt(inst: str, pc: int) -> tuple:
    return pc+1, True


def addf(inst: str, pc: int) -> tuple:
    reg1_value, reg2_value = typeFloat(inst)
    reg3_value = reg2_value + reg1_value
    if (setFracRegValue(reg3_value, inst[13:])):
        return pc+1, True
    return pc+1, False


def subf(inst: str, pc: int) -> tuple:
    reg1_value, reg2_value = typeFloat(inst)
    reg3_value = reg1_value - reg2_value
    if (setFracRegValue(reg3_value, inst[13:])):
        return pc+1, True
    return pc+1, False


def movf(inst: str, pc: int) -> tuple:
    # Convert the IEEE value to a float value
    ImmVal = convertFromIEEE(inst[8:])
    # convert that float back into standard binary
    ImmVal = convertToIEEE(ImmVal)
    ImmVal = getDecimal(ImmVal)        # convert that binary to decimal
    setRegValue(ImmVal, inst[5:8])     # and store in register
    return pc+1, False


mapping = {
    '10000': add,
    '10001': sub,
    '10110': mul,
    '11010': xor,
    '11011': or1,
    '11100': and1,
    '00000': addf,
    '00001': subf,
    '10010': mov,
    '11000': rs,
    '11001': ls,
    '00010': movf,
    '10011': movr,
    '10111': div,
    '11101': not1,
    '11110': cmp,
    '10100': ld,
    '10101': st,
    '11111': jmp,
    '01100': jlt,
    '01101': jgt,
    '01111': je,
    '01010': hlt
}


def main():
    add("1011000011001010")
    pass


if __name__ == "__main__":
    main()
