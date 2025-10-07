file = open('text.txt','r')
print(file.read())
file.close()

file = open('text.txt','r')
print("\nRead in parts \n")
print(file.read(8))
file.close()


file = open('Codingal.txt','a')
file.write("\n Hi! I am Penguin and I am 1 yr old.")
file.close()