mydict={

}
n=int(input().strip())
e=[]
for i in range(0,n):
    k=input()
    e.append(k)
s=set(map(str,e))
print(len(s))