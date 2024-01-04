def divisible5(l):
    if l%5==0:
        return True
    else:
        return False 

l=[21,25,45,91,90,75]
print("orignal list ",l)
print("Filtered list: ",list(filter(divisible5,l)))