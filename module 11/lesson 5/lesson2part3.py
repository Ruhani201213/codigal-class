file1 = open('text.txt','r')
file2 = open('text2.txt','w')

for line in file1.readlines():

    if not (line.startswith('pengun')):

# printing those lines
    print(line)


file2.write(line)

file2.close()
file1.close()