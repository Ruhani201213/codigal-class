num= int(input("enter number to multiply:"))
print(f"table of {num}")
for i in range(1,11):
    mul = num*i
    print("%d x %d = %d"% (num,i,mul))