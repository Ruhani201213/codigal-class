with open('codigalfile') as fp:
    data1=fp.read()
with open('sample.txt') as fp:
    data2=fp.read()

data1+="\n"
data1=data1+data2
print("merging two files....")
with open ('MergedFile.txt', 'w') as fp:
    fp.write(data1)