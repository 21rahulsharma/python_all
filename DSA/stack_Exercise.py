#String Traversal Using Stack
from collections import deque
class stackex:
    def __init__ (self):
        self.c=deque()
    def intake(self):
        n=input("Enter a string").strip()
        for i in n:
            self.c.append(i)
        l=len(self.c)
        for i in range(l):
            print(self.c.pop(),end="")
s=stackex()
s.intake()