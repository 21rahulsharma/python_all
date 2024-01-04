a=1
class rahul:
    def __init__(self,info):
        self.info=info
        global a 
        print(f"object {a} is called ")
        a+=1

    def member(self,data):
        self.data=79
objec1=rahul(67)
objec1=rahul(56)
objec1=rahul(99)




# strink=input("Enter a string").split()
# print(len(strink))