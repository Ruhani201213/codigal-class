def factorial(n):
    if n<0:
        print("number invalid")
    elif n == 1 or n == 0 :
        return(1)
    return(n*factorial(n-1))
n=int(input("enter an number to find its factorial"))
factorial_=factorial(n)
try:
    print("%d! = %d"%(n,factorial_))
except:
    print(factorial_)
