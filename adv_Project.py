class library:

    def __init__(self,list_of_books):
        self.books=list_of_books
    def display(self):
        print(f"The books present  in this library are:")
        c=1
        for i in self.books:
            
            print(f"\t {c}) {i}")
            c+=1

    def borrow(self,bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname} & please Return it within 30days to avoid Penalty \n Happy Reading!")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry, This Book has been issued to someone else. We will intimate you as soon as it is returned by the issuer ")
            return False
    def returnbook(self,bookreturn):
        self.books.append(bookreturn)
        print("Thanks for Returning the book ")


class student:
    def req(self):
        reqbook=input("Enter The name of the book you want to borrrow: ")
        self.book=reqbook
        return self.book
    def returnb(self):
        self.book=input("Enter th name of the book you want to return: ")
        return self.book
    pass
if __name__=="__main__" :
    list=["SQL Black Book","Advanced C++","Bhagavat Gita","Core Java","Mastering HTML,CSS,JS","Web development for beginnners","Cracking The Coding Interview","Rich Dad Poor Dad","You can win","Wings of Fire","Why I am Atheist"]
    list2=list
    l=library(list)
    s=student()
    # l.display()
    while(True):
        msg='''
        1.Listing all the books in the Library 
        2.Request a book 
        3.Return a book 
        4.Exit the library '''
        print("Welcome to Central Library")
        print("Please chose an Option:-")
        a=int(input(msg))
        if a==1:
            l.display()
        elif a==2:
            l.borrow(s.req())
        elif a==3:
            l.returnbook(s.returnb())
        elif a==4:
            print("Thanks for Choosing Central Library ")
            exit()
        else:
            print("Invalid Choice, Choose Again!")
