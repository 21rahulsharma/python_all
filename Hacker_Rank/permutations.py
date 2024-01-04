from itertools import permutations
n,r=input().split()
r=int(r)
l=list(permutations(n,r))
l.sort()
for elements in l:
    length=len(elements)
    for i in range(0,length):
        print(elements[i],end="")
    print("\n")
    