class Number :
    company="google "
    def __init__(self,name,salary,subunit) :
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created")
    def getdetails(self):
        print(f"salary of employee={self.salary} and is working in {self.subunit} ")

    def sum(self):
        print(self.company)
        return self.a+self.b
    @staticmethod
    def greet():
        print("hello rahul !")
        
harry= Number("harry",100000,"printers")
harry.getdetails()
harry.greet()
