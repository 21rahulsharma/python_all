def swap_case(s):
    new=''
    for i in s:
        if i.isupper():
            new+=i.lower()
        elif i.islower():
            new+=i.upper()
        else:
            new+=i
    return new

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)