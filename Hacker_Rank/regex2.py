import re
n=int(input().strip())
for i in range(n):
    s=input().strip()
    try:
        
        print(re.compile(s))
    except:
        print(False)