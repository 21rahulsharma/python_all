st=input("Enter a string ")
from collections import deque
class stack_using_deque:
    def __init__(self):
        self.c=deque()
    def push(self,val):
      self.c.append(val)
    def pop(self): 
        return self.c.pop()
    def peak(self):
      return self.c[-1]
    def empty(self):
      return len(self.c)==0
    def size(self):
      return len(self.c)
s=stack_using_deque()
for i in st :
    s.push(i)
str=''
while s.size()!=0:
   str+=s.pop()
print(str)
    