class Employee:
    def __init__(self,sal,increment):
        self.sal=sal;
        self.incr=increment;
    @property
    def totalsalary(self):
        return self.sal+self.incr
    @totalsalary.setter
    def totalsalary(self,val):
        self.incr=val*0.1
e=Employee(85000,5600)
v=e.totalsalary
print("The total salary=",v)




