
siz_m=input()
m=input().split()
set1=set(map(int,m))
size_n=input()
n=input().split()
set2=set(map(int,n))
set3=set()
set3.update(set1.difference(set2))
set3.update(set2.difference(set1))
sorted(set3)
for i in set3:
    print(i)

