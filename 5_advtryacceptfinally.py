from re import I


try:
    i=int(input("Enter a no."))
    c=1/i  
except Exception as e:
       print(e)
finally:
    print("We r done")
    
