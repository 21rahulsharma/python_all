'''a=
b=34
print("sum=",a+b) '''   #procedure oriented programming 

class Number :
    def sum(self):
        return self.a+self.b
    @staticmethod
    def greet():
        print("hello rahul !")

num= Number()
num.a=51
num.b=34
s=num.sum()
print(s)
num.greet()