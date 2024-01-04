word1="Rahul"
word2="sir"
l1=len(word1)
l2=len(word2)
m=max(l1,l2)
print(m)
newstr=""
for i in range(0,m+1):
    if(i<l1):
        newstr=newstr+word1[i]
    if(i<l2):
        newstr=newstr+word2[i]
print(newstr)