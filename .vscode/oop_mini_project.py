#Create a library class
# display Book
#lend book(who owns the book if not present in library (lena chahta hai))
#add book
#return book
#harryLibrary=Library(listofbook, library_name)
# dictionary(books-nameofperson)
from os import remove
class library: 
    returnBooks=[]
    totalBooks=[]
    def __init__(self,listOfBook) -> None:
        self.books=listOfBook        
           
            
    def updateBook(self):
        for readB in self.books:
            self.totalBooks.append(readB)
                
     
    def displayofBooklist(self):
        self.updateBook() 
        for book in self.books:            
            print(f"{book}")
            
    def BorrowBook(self):   
                    
        self.bbook =input("Please Enter Book name : ")
        if  self.bbook in self.totalBooks:
            print(f"Congratulatoin you are borrow the {self.bbook}, please keep and safe")
            self.totalBooks.remove(self.bbook)    
            self.returnBooks.append(self.bbook)
            
        else:
            print("Sorry! you wait untile return the book")
            
    def returnBook(self): 
        self.rbbook =input("Please Enter Return Book name : ")
        print("Thanks for return a book for next student! have a nice day")
        self.returnBooks.remove(self.rbbook)   
        self.totalBooks.append(self.rbbook)    

    def StatusofBook(self):
        print(f"Total avalable Book in library{self.totalBooks}")
        print(f"Total Borrow Book in library{self.returnBooks}")       
def funlibrary():
    print ("""Welcom to My Library
           1. for Display of Books,2. for Borrow a Book from library, 3. for Return a Book, 4. Status of Library Books,5. for Exit""")    
    kk =library(["Django","Ramayan","Mahabharat","Shivpuran","Sushila"])
    # kk.displayofBooklist()
    # kk.BorrowBook()     
    studentinput=int(input("please Enter your choise  "))
    if studentinput==1:
        kk.displayofBooklist()
        funlibrary()
    elif studentinput==2:
        kk.BorrowBook()
        funlibrary()
    elif studentinput==3:
        kk.returnBook()
        funlibrary()
    elif studentinput==4:
        kk.StatusofBook()
        funlibrary()
    elif studentinput==5:
        exit()
    else:
        print("please Enter a valid choice")  
        funlibrary()   
           
funlibrary()    
    

           
        
        
              
    
