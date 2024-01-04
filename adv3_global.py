a=78
b=45
def func1():
    global a #Writen in order to use global a instead of creating a local variable'a'
   
    print(a)   #As global is written the global value of a will be used
    a=5        #now the global value of a is set to 5
    b=10
    print(a,  b)

func1()
print(a,   b)