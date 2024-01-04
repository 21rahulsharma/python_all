from collections import deque
class balance:
    def __init__ (self):
        self.c=deque()
    def match(self,a1,a2):
        mydict={
            ')':'(',
            '}':'{',
            ']':'['
        }
        return mydict[a1]==a2
    def intake(self):
        n=input("Enter the values").strip()
        set1={']','}',')'}
        set2={'[','{','('}
        flag='Positive'
    
        for i in n:
            if i in set2:
                self.c.append(i)
                print(self.c)
            elif i in set1:
                if len(self.c)==0:
                    return False
                
                if not self.match(i,self.c.pop()):
                    return False
                
        
s=balance()
r=s.intake()
if r==False:
    print("Not Balanced")
else:
    print("Balanced")
