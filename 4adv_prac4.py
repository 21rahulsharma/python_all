print("Enter the value of a and b ")
a=int(input("a= "))
b=int(input("b= "))
try:
    f=a/b
    print(f"The value of a/b ={f}")
except ZeroDivisionError:
    print("Infinite")

