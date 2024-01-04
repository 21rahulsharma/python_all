n=input("Enter a number ").strip()
k=int(input("Enter the alue of k ").strip())
while(k!=0):
    for i in range(len(n)):
        if(n[i]>n[i+1]):
            n=n[:i]+n[i+1:]
            k-=1
            print(n)
            break
print(int(n))
