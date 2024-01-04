a=int(input("Enter a number :"))
s=0
for i in range(2,a):
    if(a%i == 0):
        s+=1
if(s!=0):
    print("It is not a prime number")
else:
    print("Its prime")
