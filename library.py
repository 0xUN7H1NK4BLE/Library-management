class library:

    def __init__(self,listofbooks):
        self.books= listofbooks

    def displayAvailablebooks(self):
        print("Books present in this librery are: ")
        for book in self.books:
            print("    *"+book)

    def Borrowbooks(self,BookName):
        if BookName in self.books:
            print(f"you have borrow {BookName}. Please return in time.")
            self.books.remove(BookName)
            return True
        else:
            print(f"sorry,{BookName} is already issued to someone else or not available so please wait")
            return False

    def returnBook(self,BookName):
        self.books.append(BookName)
        print("thanks for returning this book!!")
        


class student:
    def requestbook(self):
        self.book=input("Enter the book you want to borrow: ")
        return self.book
    def returnbooks(self):
        self.book=input("Enter the book you want to return: ")
        return self.book

if __name__ == "__main__":
    AnishLibrary=library(["math","science","english","nepali","moral","physics"])
    students=student()
   # AnishLibrary.requestbook()
    #AnishLibrary.displayAvailablebooks()
    while(True):
        welcomeMsg="""*****welcome to Anish Library*****
        Please choose an option:
        1.List of all books
        2.request a book
        3.return or donate a book
        4.exit the Library"""
        print(str(welcomeMsg))
        a=int(input("Enter a choice: "))
      

        if a==1:

         AnishLibrary.displayAvailablebooks()
        elif a==2:
            #req=student()
            #req.requestbook()
            AnishLibrary.Borrowbooks(students.requestbook())
        elif a==3:
         #students.returnbooks()
         AnishLibrary.returnBook(students.returnbooks())
        elif a==4:
            print("thanks for choosing anish library !!")
            exit()

        else:
            print("invalide choice!!")


            
              