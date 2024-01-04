class Employee:
    company="Cisco"
    salary=82000  #class attribute
    location="Bbsr"        

    '''def changesal(self,sal):
        self.salary=sal '''  #instance attribute
 
                   #to change both class and instance attributes
    @classmethod   #to access & change class attributes
    def changesal(cls,sal):  #cls=class
        cls.salary=sal



e= Employee ()
print(e.salary)
e.changesal(9700)
print(e.salary)
print(Employee.salary)
