import time
import threading
from collections import deque
class queue_implementation:
    def __init__(self):
        self.c=deque()
        self.i=0
    def placeorder(self,ordlist):
        for j in ordlist:
            time.sleep(0.2)
            
            self.c.append(f"Order {j} ")
        
    def serveorder(self):
        time.sleep(2)
        l=len(self.c)
        for i in range(l):
            time.sleep(2)
            print(f"{self.c.popleft()} is Ready")
q=queue_implementation()
n=['Pizza','Samosa','Biriyani','Pasta','Burger']
t1=threading.Thread(target=q.placeorder,args=(n,))
t2=threading.Thread(target=q.serveorder)
t1.start()
t2.start()

    

