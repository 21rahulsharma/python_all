def happy(l,i1,i2):
    count=0
    s1=set(map(int,i1))
    s2=set(map(int,i2))
    for i in l:
        if(i in s1):
            count+=1
        elif(i in s2):
            count-=1
    print(l)
    print(s1)
    print(s2)
    print(count)
        
if __name__=="__main__":
    # m,n=input().split()
    
  
    l=input().split()
    l=list(map(int,l))
    i1=input().split()
    i2=input().split()
    happy(l,i1,i2)
