number=int(input("enter number to check whether even or odd"))
print("number to be checked:",number)
if number >50:
    print(number,"","is lesser than 50")
    if number%2==0:
        print(number,"","is even")
    else:
        print(number,"","is odd")



else:
    print(number,"","is greater then 50")