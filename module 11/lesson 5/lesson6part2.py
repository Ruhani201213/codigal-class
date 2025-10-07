file=open('text.txt',"r")
print("file is now in read mode:")
print(file.read())
file.close()

file_write=open('text.txt',"w")
file_write.write("file is now in write mode:")
file_write.close()

file_append=open('text.txt',"a")
file_append.write("file is now in append mode:")
file_append.close()