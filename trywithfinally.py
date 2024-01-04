try:
    i=int(input("Enter a number"))
    c=1/i;
except Exception as e:
    print(e)
    exit() #Keyword to exit program

finally:
    print("We are done")
print("After exiting the program ,nothing other than finally will be executed ")