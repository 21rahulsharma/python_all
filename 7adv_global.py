a=54  #Global variable
b=7    #Global variable
def func1():
    a=8             #local variable
    global b         #keyword to use global variable'b'
    print(b)
    
    b=17         #local variable
   
    print(a)
    print(b)
func1()
print(a)
print(b)