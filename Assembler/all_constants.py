"""Program where all the data from the json files
will be extracted and stored in python for ease of access"""

import json
import pprint

inst = {}
with open("ISA_Instructions.json") as f:
    inst = json.load(f)

