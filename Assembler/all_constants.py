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

    terms = f[terms]
    no_of_register = f[no_of_register]
    unused_bits = f[unused_bits]
    memory_bits = f[memory_bits]
    immediate_values = f[immediate_values]
    register_addr = f[register_addr]
