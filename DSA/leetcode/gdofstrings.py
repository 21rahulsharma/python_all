str1="ABABAB"
str2="ABAB"
str0=""
m=min(len(str1),len(str2))
for i in range(0,m):
    if str1[i]==str2[i]:
        if(len(str0)>0):
            if str1[i]==str0[0]:
                break
        str0=str0+str1[i]
    else:
        str0=""
print(str0)