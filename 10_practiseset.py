class programmer: 

    company="Microsoft"
    def __init__(self,name,salary):     #constructor
        self.name=name
        self.salary=salary
        
    def storeinfo(self):
        self.name=input("Enter name of employee")
        self.salary=input('Enter salary')
        self.unit=input("enter division")
    def printinfo(self,company):
        
        print(f"Name of company: {company} Name of Employee: {self.name} salary: {self.salary}")
hari=programmer("Hari",42000)            #object1 created for employee "hari"
hari.storeinfo()
hari.printinfo("TCS")
shyam=programmer("Shyam",35000)                 #object2 created for employee "shyam"
shyam.printinfo("TCS")
