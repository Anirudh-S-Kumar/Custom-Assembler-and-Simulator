"""Program where all the data from the json files
will be extracted and stored in python for ease of access"""

import json
import pprint


# Defining the dictionaries
inst = terms = no_of_register = {}
unused_bits = memory_bits = {}
immediate_values = register_addr = {}


#Extracting data from them
with open("ISA_Instructions.json") as f:
    inst = json.load(f)
with open("other_constants.json") as f:
    temp = json.load(f)
    terms = temp["terms"]
    no_of_register = temp["no_of_registers"]
    unused_bits = temp["unused_bits"]
    memory_bits = temp["memory_bits"]
    immediate_values = temp["immediate_values"]
    register_addr = temp["register_addr"]

# For testing
def main():
    pprint.pprint(register_addr)

if __name__ == "__main__":
    main()