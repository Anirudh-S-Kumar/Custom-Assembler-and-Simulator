import sys, os

abs_path = os.path.split(os.getcwd())[0] + "/CO_Project/" 
sys.path.append(abs_path + "/Simple-Assembler")

import all_constants



def getRegValue(address: str) -> int:
    """
    Gets the value from the passed address. Address must be of the register
    """
    pass