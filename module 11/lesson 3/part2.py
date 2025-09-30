class student:
    grade = 8
    name = "ruhani"


    def introduction(self):
        print("hiii, i am a student  ")


    def details(self):
        print("my name is",self.name)
        print("my grade is",self.grade)

ob = student()
ob.introduction()
ob.details()