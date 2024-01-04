a=[3,6,87,999,2,43,11,543,890,91,200,21]
b=[]
a.sort()
a.pop(11)
a.remove(543,)
a.insert(5,35)
print(len(a))
a.pop(10)
print(a)
''' for item in a:
    if item%2==0:       
        b.append(item)    #alternative of the code below
print(b) '''
b=[i for i in a if i%2==0 ]
print(b)