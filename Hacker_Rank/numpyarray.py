import numpy
n=int(input("Enter the number of Rows").strip())
listof=[]
for i in range(n):
    k=list(map(int,input("Enter Space Separated Numbers ").split()))
    listof.append(k)
myarr=numpy.array(listof)
p=numpy.max(myarr,axis=0)
print(p)