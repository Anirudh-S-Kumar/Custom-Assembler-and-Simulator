import pprint
from simulator_constants import register



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

def reset_flags() -> None:
    setRegValue(0, "111")


def overflow_flag(value: int) -> None:
    """Raises overflow flag if value is more than 255, or less than 0"""
    if not (-1 < value < 256):
        flag = getRegValue("111")
        flag+=8 # same as making the flag bit 1
        setRegValue(flag, "111")

def comparison_flag(reg1: int, reg2: int) -> None:
    """Raises the greater than, less than, or equal to flag depending on the inputs"""
    flag = getRegValue("111")

    if reg2 > reg1:     flag+=2
    elif reg2 < reg1:   flag+=4
    else:               flag+=1

    setRegValue(flag, "111")            



def main():
    overflow_flag(1111)

if __name__ == "__main__":
    main()