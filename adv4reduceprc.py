from functools import reduce
def maximum(a,b,c):
    x=max(a,b,c)
    return x
    
    

l=[2,54,89,1,35,21,56,78]
print(f"The Largest Number in the list is {reduce(max,l)}")