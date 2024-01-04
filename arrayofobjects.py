import random
l=[]
sub=[]
sub2=[]
n=int(input("Enter the number of elements in the array"))
# for i in range(0,n):
#     l[i]=random.randint(0,n)
# print(l)
print("Enter values into the array")
for i in range(0,n):
    e=int(input(f"Enter element No. {i+1} : "))
    l.append(e)
subarraysize=int(input("Enter the size of sub-array 'm': "))
subarrayc=subarraysize
subarrayqty=int(input("Enter the no of subarrays you want to create 'n': "))
if (subarrayc*subarrayqty)>n:
    print("Enter valid values for k & m ")
    exit();
c=0
for i in range(0,subarrayqty):

    sub=[]
    subarraysize=subarrayc
    while(subarraysize!=0):
        
        sub.append(l[c])
        if(c<n-1):
            if(l[c]==l[c+1]):
                
                subarraysize+=1
            
        c+=1
        subarraysize-=1
    
    if i>0:
        if(sub2==sub):
            print("Cannot Create such Sub string")
            break
    
    sub2=sub
    print(f"{sub2}, ")



            
        
            
        


