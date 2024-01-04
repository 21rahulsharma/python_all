import time
import threading
def calsq(num):
    for i in num:
        time.sleep(0.2)
        print("SQure of the Number=",i*i)
def cube(num):
    for i in num:
        time.sleep(0.2)
        print("Cube of the number= ",i*i*i )
n=[5,7,9]
t=time.time()
# calsq(n)
# cube(n)
t1=threading.Thread(target=calsq,args=(n,))
t2=threading.Thread(target=cube,args=(n,))
t1.start()
t2.start()
t1.join()#Wait till t1 finishes then proceed to statements below
t2.join()
print("Done in:",time.time()-t)