class complex:
    def __init__(self,real,imaginary):
        self.r=real;
        self.i=imaginary
    def __add__(self,c):
        return complex(self.r+c.r,self.i+c.i)
    def __mul__(self,c):
        mulReal =(self.r*c.r+self.i*c.i)
        mulImaginary =(self.r*c.i+self.i*c.r)
        return complex(mulReal,mulImaginary)
    def __str__(self):
        if self.i<0:
            return f"{self.r}  {self.i}i"
        else:
            return f"{self.r} + {self.i}i"

c1=complex(1,-4)
c2=complex(8,-5)
print(c1+c2) #addiion of 2 objects invokes __add__
print(c1*c2)
print(c1)