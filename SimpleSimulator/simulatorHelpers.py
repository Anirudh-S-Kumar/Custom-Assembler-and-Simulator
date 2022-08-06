from assemblerHelpers import validFloat, exponentCount
from simulatorConstants import register, memory, rFlag
from math import log2, floor
import sys
import os

abs_path = os.path.split(os.getcwd())[0]
sys.path.append(abs_path + "/Simple-Assembler")


def convertToIEEE(value: float) -> str:
    """
    Returns a 16 bit string of the floating point notation of the number
    Assumes that value can be represented in the given format
    """
    exponent = floor(log2(value))
    mantissa = ((value / (2 ** exponent)) - 1)
    floatBase2 = []
    for i in range(5):
        floatBase2.append(str(int((mantissa * 2) // 1)))
        mantissa = (mantissa * 2) - ((mantissa * 2) // 1)

    rval = ("0" * 8) + "{0:03b}".format(exponent) + "".join(floatBase2)
    return rval


def convertFromIEEE(value: str) -> float:
    """
    Return floating point value of string in 16 bits
    """
    exponent = int(value[:3], 2)
    mantissa = 2**5 + int(value[3:], 2)
    rval = mantissa * 2 ** (exponent - 5)
    rval = rval
    return rval


def getRegValue(address: str) -> int:
    """
    Gets the value from the passed address. Address must be of the register
    """
    internalDict = register[address]
    return list(internalDict.values())[0]


def getFracRegValue(address: str) -> float:
    """
    Takes the last 8 bits of the register value and converts them into float
    """
    internalDict = register[address]
    valBase2 = base2Bit16(list(internalDict.values())[0])
    valBase2 = valBase2[8:]

    return convertFromIEEE(valBase2)


def setRegValue(value: int, address: str) -> None:
    """
    Sets the given value at given address
    """
    internalDict = register[address]
    key = list(internalDict.keys())[0]
    internalDict[key] = value
    # print("setRegValue : ", rFlag)


def setFracRegValue(value: float, address: str) -> bool:
    """
    Sets value of register to the register after converting it to binary, and then back to decimal
    Sets value to 0 if there is precision error
    Returns true for overflow, False for not overflow
    """
    internalDict = register[address]
    key = list(internalDict.keys())[0]

    if (validFloat(value)) and (1 <= value <= 252):
        base2 = convertToIEEE(value)
        internalDict[key] = getDecimal(base2)
        return True

    internalDict[key] = 0
    setRegValue(8, "111")
    return False


def getDecimal(value: str) -> int:
    """
    Returns the base 10 value of the immediate value
    For now, the value is assumed to be in unsigned base 2
    """

    return int(value, base=2)


def getVarValue(address: str) -> int:
    """
    address is the 8 bit value of address of the particular variable
    """
    memAdd = getDecimal(address)  # converts the 8 bit value into decimal
    varVal = getDecimal(memory[memAdd])
    return varVal


def setVarValue(address: str, val: int) -> None:
    """
    address is the 8 bit value of address of the particular variable
    """
    memAdd = getDecimal(address)  # converts the 8 bit value into decimal
    memory[memAdd] = base2Bit16(val)


def resetFlags() -> None:
    setRegValue(0, "111")


def overflowFlag(value: int) -> bool:
    """Returns true and Raises overflow flag if value is more than 255, or less than 0"""
    if not (-1 < value < 2**16 - 1):
        flag = getRegValue("111")
        flag += 8  # same as making the flag bit 1
        setRegValue(flag, "111")
        return True
    return False


def comparisonFlag(reg1: int, reg2: int) -> bool:
    """Raises the greater than, less than, or equal to flag depending on the inputs"""
    flag = getRegValue("111")

    if reg1 > reg2:
        flag += 2
    elif reg1 < reg2:
        flag += 4
    else:
        flag += 1
    # print("called")
    # print('comparison :', flag)
    setRegValue(flag, "111")


def base2Bit8(value: int) -> str:
    return "{0:08b}".format(value)


def base2Bit16(value: int) -> str:
    return "{0:016b}".format(value)


def dumpRegs():
    """
    Prints the values of all the registers in base 2
    """
    output_list = []
    for i in (register):
        temp = getRegValue(i)
        output_list.append(base2Bit16(temp))
    print(" ".join(output_list))


def memoryDump() -> None:
    for i in memory:
        print(i)


def main():
    print(setFracRegValue(4.0625, "000"))


if __name__ == "__main__":
    main()
