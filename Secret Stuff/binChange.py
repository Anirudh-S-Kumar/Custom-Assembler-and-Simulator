from os import listdir

dirs = [i for i in listdir() if i[-2:] != 'py']

for j in dirs:
    with open(j) as f:
        text = f.readlines()
        text = [i.rstrip('\n') for i in text]
        updated = []
        temp = ""
        for i in text:
            if i[0] == "0":
                temp = "1" + i[1:]
                
                if temp[0:5] == "10011":
                    temp = list(temp)
                    temp[10:13] , temp[13:16] = temp[13:16], temp[10:13]
                    temp = "".join(temp)


            else:
                first_5 = i[0:5]
                if first_5 == "10000":
                    temp = "01100"
                elif first_5 == "10001":
                    temp = "01101"
                elif first_5 == "10010":
                    temp = "01111"
                elif first_5 == "10011":
                    temp = "01010"
                
                temp = temp + i[5:]
            
            temp = temp + "\n"
            updated.append(temp)

        print(updated)
        with open(j, "w") as f:
            f.writelines(updated)
        
        print(j)
