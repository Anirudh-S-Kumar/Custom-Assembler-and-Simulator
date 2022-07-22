#Q5(Bonus Question)

Dict = {'Bit addressable memory' : 1 ,'Nibble addressable memory' : 4, 'Byte addressable memory' : 8} #In this dictionary Key is addressable memory and value is cell size.

#Type 1
#initial input
memory_space = input()  
#Type1 function
def type1(memory_space,Dict):
    a = int(memory_space[0])/8             #conversion to bytes
    b = a/1024                       #conversion to KB
    b = b/1024                       #conversion to MB  
    b = b/1024

    bitCPU = input() #Number of bits in CPU
    bitCPU = bitCPU.split()
    address_memory = input()   #enhanced addressable memory




#Type 2

bitCPU = input() #Number of bits in CPU
bitCPU = bitCPU.split()
address_pins = input() #Number of address pins
address_pins = address_pins.split()
address_memory = input() #Type of addressable memory

number_address = 2**int(address_pins[0])  #possible number of memory address

if(address_memory in Dict):
    a = number_address/8             #conversion to bytes
    b = a/1024                       #conversion to KB
    b = b/1024                       #conversion to MB  
    b = b/1024                       #conversion to GB

    final_output = Dict[address_memory]*b
    print(int(final_output),'GB')

elif(address_memory == "Word addressable memory"):
    a = number_address/8             #conversion to bytes
    b = a/1024                       #conversion to KB
    b = b/1024                       #conversion to MB  
    b = b/1024                       #conversion to GB

    final_output = b*int(bitCPU[0])
    print(int(final_output),"GB")







    
        





