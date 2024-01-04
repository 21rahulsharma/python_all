with open('poems.txt','r') as f:
    a=f.read()
print(a)
if a.count("twinkle")>-1:
    print("The word twinkle exists in the file 'poems.txt'")
