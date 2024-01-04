from itertools import permutations
n=input("Enter a number ").strip()
p=permutations(n)
p=list(p)
p.sort()
for i in p:
    print(i)