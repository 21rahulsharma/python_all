while(True):
    print("Press q to quit")
    a=input("enter a number ")
    if a=='q':
        break
    try:
        a=int(a) #typecasting
        
        if a>6:
            print("Number greater than 6 ")
        
    except Exception as e: 
        print(f"Your input resulted in an error{e}")
        print("Enter a valid value ")
    
print("Thanks")

