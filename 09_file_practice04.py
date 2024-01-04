with open('sample1file.txt','r+') as f :
    d=f.read()
    e=d
    c=d.count("Dairy Milk")
    print("count= ",c)

    