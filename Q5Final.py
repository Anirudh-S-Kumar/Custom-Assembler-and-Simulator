#5(Bonus Question)
import math
print("-------------------------------------Type 1------------------------------------------")
print()
Dict = {'Bit addressable memory' : 1 ,'Nibble addressable memory' : 4, 'Byte addressable memory' : 8} 

#Type1

inst_length=int(input("Enter your Instruction Length: "))
reg_length=int(input("Enter Register Length: "))

#Initial input

inp_mem=input("Input Memory: ")
inp_mem=inp_mem.split()
bits=int(inp_mem[0])*(2**10)
x = math.log(bits) / math.log(2)
#print(x)
print()
print("1.Bit addressable memory")
print("2.Byte addressable memory")
print("3.Nibble addressable memory")
print("4.Word addressable memory: ")
print()
address_type=input("Enter Address Type: ")
if(address_type=="Byte addressable memory"):
    address_pins=2**x/2**3
    y=math.log(address_pins)/math.log(2)

elif(address_type=="Nibble addressable memory"):
    address_pins=2**x/2**2
    y=math.log(address_pins)/math.log(2)

elif(address_type=="Bit addressable memory"):
    address_pins=2**x/2**1
    y=math.log(address_pins)/math.log(2)

elif(address_type=="Word addressable memory"):
    address_pins=2**x/2**4
    y=math.log(address_pins)/math.log(2)

print()
print("The minimum bits needed for architecture: ", y)
print("The number of bits need by opcode: ",inst_length - y - reg_length)
print("The number of filler bits in Instruction type 2: ",inst_length - (inst_length - y - reg_length) - reg_length - reg_length)
print("Maximum numbers of instructions this ISA can support: ",2**(inst_length-y-reg_length))
print("Maximum number of registers this ISA can support: ",2**reg_length)
print()

#type 2 PART 1
bitCPU=int(input("Enter the number bits in CPU: "))
address_type2=input("Enter the address type to be converted: ")
if(address_type2=="Word addressable memory"):
    g=math.log(bitCPU)/math.log(2)
    print()
    new_pins=2**x/2**g

elif(address_type2=='Byte addressable memory'):
    print()
    new_pins=2**x/2**3

elif(address_type2=='Bit addressable memory'):
    print()
    new_pins=2**x/2

elif(address_type2=='Nibble addressable memory'):
    print()
    new_pins=2**x/2**2

z=math.log(new_pins)/math.log(2)
output=y-z
if(y>z):
    print("Number of pins saved: -",int(output))

else:
    print("Number of pins required: +",int(output))

print()
print("-------------------------------------Type 2------------------------------------------")
print()
bitCPU = input("Enter the number bits in CPU: ") #Number of bits in CPU
bitCPU = bitCPU.split()
address_pins = input("Enter the number of address pins: ") #Number of address pins
address_pins = address_pins.split()
print()
print("1.Bit addressable memory")
print("2.Byte addressable memory")
print("3.Nibble addressable memory")
print("4.Word addressable memory")
print()
address_memory = input("Enter the type of addressable memory: ") #Type of addressable memory

number_address = 2**int(address_pins[0])  #possible number of memory address

if(address_memory in Dict):
    a = number_address/8             #conversion to bytes
    b = a/1024                       #conversion to KB
    b = b/1024                       #conversion to MB  
    b = b/1024                       #conversion to GB

    print()
    final_output = Dict[address_memory]*b
    print(int(final_output),'GB')

elif(address_memory == "Word addressable memory"):
    a = number_address/8             #conversion to bytes
    b = a/1024                       #conversion to KB
    b = b/1024                       #conversion to MB  
    b = b/1024                       #conversion to GB

    print()
    final_output = b*int(bitCPU[0])
    print(int(final_output),"GB")
