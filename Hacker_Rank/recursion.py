

def fact(n):
    if n>1:
        
        return (n*fact(n-1))
    else:
        return 1
    
    

a=int(input("Enter a number: "))
na=fact(a)
print(na)