def solve(s):
    e=""
    p=s.split()
    q=list(map(str,p))
    print(q)
    l2=(i.capitalize() for i in q)
    e=" ".join(l2)
    return e
if __name__ == '__main__':
    

    s = input()

    result = solve(s)

    print(result + '\n')
