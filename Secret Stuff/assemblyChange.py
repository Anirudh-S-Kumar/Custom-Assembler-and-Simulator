from os import listdir

dirs = [i for i in listdir() if i[-2:] != "py"]

for i in dirs:
    final = []
    with open(i) as f:
        text = f.readlines()
        text = [i.rstrip('\n') for i in text]
        print()
        for j in text:
            if j:
                j = j.split()
                print(j)
                if j[0] == "mov":
                    if j[2][0] != "$":
                        j[1], j[2] = j[2], j[1]
                
                final.append(" ".join(j) + "\n")
    
    with open(i, "w") as f:
        f.writelines(final)
    
    print("done")
