#No collision handling mechanism
class hash_table:
    def __init__(self):
        self.max=100
        self.arr=[None for i in range(self.max)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%100
    def add(self,key,value):
        h=self.get_hash(key)
        self.arr[h]=value
    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]
t=hash_table()
t.add("march 6",210)
print(t['march 6'])

