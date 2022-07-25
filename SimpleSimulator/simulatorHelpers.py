from simulatorConstants import register, memory, rFlag


def getRegValue(address: str) -> int:
    """
    Gets the value from the passed address. Address must be of the register
    """
    internalDict = register[address]
    return list(internalDict.values())[0]

def setRegValue(value: int, address: str) -> None:
    """
    Sets the given value at given address
    """
    internalDict = register[address]
    key = list(internalDict.keys())[0]
    internalDict[key] = value
    # print("setRegValue : ", rFlag)

def getDecimal(value:str) -> int:
    """
    Returns the base 10 value of the immediate value
    For now, the value is assumed to be in unsigned base 2 
    """
    
    return int(value, base=2)

def getVarValue(address: str) -> int:
    """
    address is the 8 bit value of address of the particular variable
    """
    memAdd = getDecimal(address) # converts the 8 bit value into decimal
    varVal = getDecimal(memory[memAdd])
    return varVal

def setVarValue(address: str, val: int) -> None:
    """
    address is the 8 bit value of address of the particular variable
    """
    memAdd = getDecimal(address) # converts the 8 bit value into decimal
    memory[memAdd] = base2Bit16(val)

def resetFlags() -> None:
    setRegValue(0, "111")


def overflowFlag(value: int) -> bool:
    """Returns true and Raises overflow flag if value is more than 255, or less than 0"""
    if not (-1 < value < 256):
        flag = getRegValue("111")
        flag+=8 # same as making the flag bit 1
        setRegValue(flag, "111")
        return True
    return False

def comparisonFlag(reg1: int, reg2: int) -> bool:
    """Raises the greater than, less than, or equal to flag depending on the inputs"""
    flag = getRegValue("111")

    if reg1 > reg2:     flag+=2
    elif reg1 < reg2:   flag+=4
    else:               flag+=1
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
    for i in register:
        temp = getRegValue(i)
        temp = base2Bit16(temp)
        print(temp, end = " ")
    print()

def memoryDump() -> None:
    for i in memory:
        print(i)

def main():
    (setRegValue(1, '111'))
    print(getRegValue('111'))

if __name__ == "__main__":
    main()