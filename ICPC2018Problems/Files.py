path = '/home/floris/Desktop/'
fileName = 'test.txt'
read = open(path + fileName,'r')
print("read1")
print(read.read())
read.close()
write = open(path + fileName, 'w')
write.write("New test moda foka!")
write.close()
print("read2")
read = open(path + fileName,'r')
print(read.read())
read.close()
