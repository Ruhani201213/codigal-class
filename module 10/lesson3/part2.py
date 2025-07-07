weight=float(input("enter weight "))
height=float(input("enter height "))
bmi=weight/(height/100)**2


print(bmi)
if bmi<25:
    print("you are underweight")
elif bmi<30:
    print("you are heathy")
elif bmi<35:
    print("you are overweight")
elif bmi<45:
    print("you are sively overweight")
elif bmi<50:
    print("you are obsese")
else:
    print("you are sively obsese")