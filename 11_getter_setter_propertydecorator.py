class Employee:
    company="cameel"
    salary=8200                                                                           #class attribute
    salary_bonus= 150
    #totalsalary = 8350
    location="Bbsr"       

    @property
    def totalsalary(self):
        return self.salary+self.salary_bonus

    @totalsalary.setter
    def totalsalary(self,val):
        self.salary_bonus = val-self.salary 


e=Employee()
print(e.totalsalary) #total salary is a property is no need for '()'
e.totalsalary = 8050
print(e.salary)
print(e.salary_bonus)