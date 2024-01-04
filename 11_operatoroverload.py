class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):            # Already Defined in python library
        print("let's add ")
        self.num2=num2
        return self.num+num2.num

n1=Number(6)
n2=Number(7)
sum=n1+n2
print(sum)
