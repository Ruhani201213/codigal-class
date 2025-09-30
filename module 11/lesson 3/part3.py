class parrot:
    type="bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age

blu=parrot("blu",10)
boo=parrot("boo",10)

print("Blu is a {}".format(blu.type))
print("boo is also a {}".format(boo.type))

print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( boo.name, boo.age))