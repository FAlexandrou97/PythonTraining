with open("cfile.txt") as file:
    for line in file.readlines():
        lineSplit = line.split()    
        N = lineSplit[0]
        L = lineSplit[1]

print(N)
print(L)