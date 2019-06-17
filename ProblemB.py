print("Enter file name: ")
fileName = input()
print("Enter flour type: ")
flour = input()

with open(fileName) as file:
    data = file.read()
    newData = data.replace("flour", flour + " flour")
    counter = 0
    result = data.split()
    counter = str(result.count("flour"))
    
with open("newfile.txt", "w") as newFile:
    newFile.write(newData)

print(counter)