def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("This is not good")    #custom messages 

a=increment('df364')
b=increment('df364')
print(a)
print(b)
