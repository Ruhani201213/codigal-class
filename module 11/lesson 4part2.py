class libary:
    def __init__(self,list_of_books,name):
        self.booklist=list_of_books
        self.name=name
        self.lendDict=[]

    def displaybook(self):
        print("we have the folloing books in our libary: {self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.booklist:
            print("sorry we do not have that book")
        elif book in lendDict:
            print("book is alreadly being used by{self.lend[book]}")
        else :
            self.lendDict[book]=user
            print("we have updated to list , you can take the book now")