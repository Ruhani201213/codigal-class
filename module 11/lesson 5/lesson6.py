class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print('i am a prowd onwer of a human,my name is {self.name} and my age is {self.age}')
    
    def makesound(self):
        print('meow')

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print('i am a dog,my name is {self.name} and my age is {self.age}')
    
    def makesound(self):
        print('wuff')
cat1=cat("kitty",3)
dog2=dog("charles",2)

for animal in(cat1,dog2):
    animal.makesound()
    animal.info()