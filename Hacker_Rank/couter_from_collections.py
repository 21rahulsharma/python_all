from collections import Counter
x=int(input("No of shoes ").strip())
size=input("Size list ").split()
s=list(map(int,size))
n=int(input("No of customers").strip())
mydict={}
mylist=[]
sum=0
for i in range(n):
    customer_req=(input("size with price").split())
    customer_reqd=list(map(int,customer_req))
    mylist.append(customer_reqd)

sizecount=Counter(s)
sizekeys=Counter(s).keys()
for element in mylist:
    if element[0] in sizekeys:
        if sizecount[element[0]]>0:
            val=sizecount[element[0]]
            sizecount[element[0]]=val-1
            sum=sum+element[1]
print(sum)
