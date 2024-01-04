import random 
def check(x,y):
    if(x==y):
        return True 
    elif(x>y):
        print("Lower number.....please!")
    else:
        print("Higher number......please!")

randomno= random.randint(1,100)
c=0
for i in range (1,12):
    #print("The program has created a number \n  ")
    b=int(input("Guess the number :"))
    c=c+1
    z=check(b,randomno)
    if(z==True):
      print(f"Congratulations....Perfect Match! \n You have guessed in number in {c} attempts ")
      break
    
# Approach-2
import random
number=random.randint(1,100)
userguess=None
guesses=0

while(userguess!=number):
    userguess=int(input("Enter your Guess"))
    guesses+=1
    if(userguess==number):
        print("You guessed it right!")
    else:
        if(userguess>number):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
print(f"You guessed the number in {guesses} guesses")