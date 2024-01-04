def count_substring(string, sub_string):
    c=0
    for i in range(len(string)):
        s=""
        k=i
        for j in range(len(sub_string)):
            if(k in range(0,len(string))):
                s=s+string[k]
                k+=1
        print(s)
        if s==sub_string:
            c+=1
    return c

if __name__ == '__main__':
    string = input("Enter a string: ").strip()
    sub_string = input("Enter a sub-string: ").strip()
    
    count = count_substring(string, sub_string)
    print(count)