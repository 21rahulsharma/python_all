#Multi-level inheritance 
class Person:
    country="India"
    #name=input("Enter your name: ")
    #salary= 29500
class staff():
    company="Maruti Suzuki"
    def getsalary(self):
        self.sal=72400
        print(f" salary= {self.sal} ")
    def change_country(self):
        self.country="England "
        print(f"country of origin is :{self.country} ")
class Employee(Person,staff ): # inheritance 
    #salary=42000
    #emid=input("Enter Employee Id ")
    def dateofbirth(self):
        print("date of birth : 21.12.1992")


class programmer (Employee):
    company="Tata Group"
    salary= 50000
    def getsalary(self):
        super().getsalary() #to call getsalary of base class 
        print(self.salary)


''' p=Person()  #func.person
print(p.country) '''
'''e=Employee()
e.dateofbirth()
print(f"Country of origin is: {e.country}")
print(f"Actual Salary of Mr.{e.name} is Rupees.: {e.salary}")'''
'''s=staff()
print(f"company> {s.company}")  #func. Staff
s.getsalary(34200) '''
p=programmer()
p.getsalary()
p.change_country()
p.getsalary()