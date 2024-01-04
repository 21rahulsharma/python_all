def merge_the_tools(string, k):
    l=len(string)
    spliting_term=l/k
    n=""
    for i in range(0,l):
        if (i+1)%k==0:
            n+=string[i]+" "
        else:
            n+=string[i]
    list=n.split()
    print(list)
    for element in list:
        wordlist=[]
        np=""#AABCAAADA
        for i in element:
            if i in wordlist:
                continue
            else:
                wordlist.append(i)
                np+=i
        print(np)

        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)