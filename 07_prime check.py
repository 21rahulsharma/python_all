num=int(input("Enter a number\n"))
c=0
for i in range(2,num):
    if num%i==0:
        c=c+1
if c>1:
    print(num,"Is a not a prime number")
else:
    print(num,"is a prime no.")