class person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class empole(person):
      def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post

        person.__init__(self,name,idnumber)

a=empole('pineapple',201213,15000,"watchman")
a.display()