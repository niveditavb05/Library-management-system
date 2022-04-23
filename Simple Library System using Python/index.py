class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day!")
        
    def addBook(self,book):
        self.books.append(book)
        print("Book has been added to your list")   

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         

if __name__ == "__main__":
    centraLibrary = Library(["JavaScript", "PHP", "C++", "Python", "Java"])
    student = Student()
    
    while(True):
        welcomeMsg = '''\n====== Welcome to Library Management System======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return a book
        4. add book
        5. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
             book=input("Enter the name of the book do you want to add:")
             centraLibrary.addBook(book)
        elif a == 5:
            print("Thanks for choosing our Library.")
            exit()
        else:
            print("Invalid Choice!")

        
