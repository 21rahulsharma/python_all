# queue=deque()
# queue.append(100)
# queue.append(200)
# queue.append(300)

# print(queue)
# queue.popleft()
# print(queue)

from collections import deque
class queue_implementation():
    def __init__(self):
        self.queue=deque()
    def insert(self,val):
        self.queue.append(val)
    def remove(self):
        
        if(len(self.queue)>0):
            s=self.queue.popleft()
        else:
            print("The Queue is Empty ")
    def __str__(self):
        return str(self.queue)
    
myqueue=queue_implementation()
myqueue.insert(100)
myqueue.insert(200)
myqueue.insert(300)
myqueue.remove()
print(myqueue)


