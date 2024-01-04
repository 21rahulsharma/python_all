import random
import time

def game(comp,b):
    if comp==b: 
        return None
    
    elif comp=='s':
        if b=='w':
            return False
        elif b=='g':
            return True
    
    elif comp=='w':
        if b=='g':
            return False
        elif b=='s':
            return True
    
    elif comp=='g':
        if b=='s':
            return False
        elif b=='w':
            return True


    pass

random_no =  random.randint(1,3)
#print(random_no)
if random_no==1:
    comp='s'
elif random_no==2:
    comp='w'
elif random_no==3:
    comp='g'

print("Lets Play!")
print("computer's turn: Snake(S), Water(W) or Gun(G) ")
time.sleep(2)
b = input("Your turn: Snake(s), Water(w) or Gun(g) ? ")
b=b.lower()
print(f"computer choose {comp}")
print(f"You chose {b}")

s=game(comp,b)  #func. call
if s == None:
    print("Game: Tied")
if s == True:
    print("You won the game!")
if s == False:
    print("You lost ..")