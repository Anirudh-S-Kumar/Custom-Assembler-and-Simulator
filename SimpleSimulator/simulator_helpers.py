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


def main():
    pass

if __name__ == "__main__":
    main()