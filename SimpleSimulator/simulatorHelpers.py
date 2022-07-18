from pprint import pprint
from simulatorConstants import register



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

def getImm(value:str) -> int:
    """
    Returns the base 10 value of the immediate value
    For now, the value is assumed to be in unsigned base 2 
    """
    rval = 0
    for i in range(8):
        rval+=int(value[i]) * (2 ** (7-i))
    
    return rval

def resetFlags() -> None:
    setRegValue(0, "111")


def overflowFlag(value: int) -> None:
    """Raises overflow flag if value is more than 255, or less than 0"""
    if not (-1 < value < 256):
        flag = getRegValue("111")
        flag+=8 # same as making the flag bit 1
        setRegValue(flag, "111")

def comparisonFlag(reg1: int, reg2: int) -> None:
    """Raises the greater than, less than, or equal to flag depending on the inputs"""
    flag = getRegValue("111")

    if reg2 > reg1:     flag+=2
    elif reg2 < reg1:   flag+=4
    else:               flag+=1

    setRegValue(flag, "111")            

def base2(value:int) -> str:
    return "{0:08b}".format(value)

def dumpRegs():
    """
    Prints the values of all the registers in base 2
    """
    for i in register:
        temp = getRegValue(i)
        # temp = base2(temp)
        print(temp, end = " ")
    print()

def main():
    dumpRegs()

if __name__ == "__main__":
    main()