a=45
b=int(input("Enter the value of b \n"))
if(a>30):
    print("value is greater than 30")
elif(a>600):
    print("value is greater than 600")
elif(a>100):
    print("greater than 100")
elif(a>=400 and a<=b): #relational operator used (and)
    print("value greater than 40 and less than 50")
if(a>50 or a>b):
    print("a is in the range : 50 to  ",b)

else:
    print("Not greater")


