 #With collision handling mechanism
class hash_table:
    def __init__(self):
        self.max=100
        self.arr=[[] for i in range(self.max)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%100
    def __getitem__ (self,key):
        h=self.get_hash(key)
        self.arr[h]
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]

        
    def __setitem__(self,key,value):
        h=self.get_hash(key)
        found=False
        for index,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][index]=(key,value)
                found=True
                break
        if not found:
            self.arr[h].append((key,value))
        return 
    def __delete_item__(self,key):
        h=self.get_hash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][index]

t=hash_table()
t["march 6"]=120
t["march 8"]=310
t["march 9"]=312
t["march 17"]=459
print(t["march 6"])
del t["march 6"]
# print(t["march 6"])


