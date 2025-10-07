file = open('text.txt','r')
print("Reading first line ... ")
print(file.readline())
file.close()

#read first three lines of file
file = open('text.txt','r')
print("Reading multiple lines ... ")
for i in range(3):
    print(file.readline)(
file.close())
    
file = open('text.txt','r')
print("Looping through the lines ... ")
for line in file:
    print(line)
file.close()