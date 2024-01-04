while(True):
    print("Press q to quit")
    a=input("enter a number ")
    if a=='q':
        break
    try:
        a=int(a) #typecasting
        b=1000/a
        print(b)
        if a>6:
            print("Number greater than 6 ")
            
    except ZeroDivisionError as e:
        print("Make sure thet you are not dividing by zero")
    except ValueError as e:
        print("Please Enter a valid value")
    except:  #If any error other than the zero-division error or value error is occurd the this is called 
        print("Enter a valid input ")
print("Thanks")

