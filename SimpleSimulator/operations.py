import helpers

# 10110 00 011 001 010

def add(inst):
    print(inst[7:10])
    reg1_value = helpers.getRegValue(inst[7:10])



def main():
    add("1011000011001010")


if __name__ == "__main__":
    main()