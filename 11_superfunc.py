#Multi-level inheritance 
from msilib.schema import SelfReg


class Person:
    country="India"
    #name=input("Enter your name: ")
    salary= 29500
class staff():
    def __init__(self) :
        print("Installing staff details..........................")
        


    company="Maruti Suzuki"
    def getsalary(self):
        self.sal=72400
        print(f" salary= {self.sal} ")
    def change_country(self):
        self.country="England "
        print(f"country of origin is :{self.country} ")
class Employee(Person,staff ): #single inheritance 
    salary=42000
    #emid=input("Enter Employee Id ")
    def dateofbirth(self):
        print("date of birth : 21.12.1992")


class programmer (Employee):
    company="Tata Group"
    def getsalary(self):
        salary= 50000
        super().getsalary() #super function
        print(f"Salary=  {salary}")

st=staff()

p=programmer()

p.getsalary()