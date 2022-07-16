from simulatorHelpers import getRegValue, setRegValue

# 10110 00 011 001 010

# Make sure to raise flags incase of underflow and overflow


def add(inst):
    print(inst[7:10])
    reg2_value = getRegValue(inst[10:13])
    reg3_value = getRegValue(inst[13:])

    reg1_value = reg2_value + reg3_value
    setRegValue(reg1_value, inst[7:10])


def main():
    add("1011000011001010")


if __name__ == "__main__":
    main()