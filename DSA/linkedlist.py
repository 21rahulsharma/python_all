class Nodel:
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next


class linkedlist:
    def __init__(self):
        self.head = None
 
    def insertatbeg(self, data):
        node = Nodel(data, self.head)
        self.head=node
        
    def print(self):
        if self.head is None:
            print("The linkedlist is empty ")
        itr = self.head
        ll = ""
        while itr:
            ll += str(itr.data)+'-->'
            itr = itr.next
        print(ll)

    def insertatend(self, data):
        if self.head == None:
            node = Nodel(data)
            self.head = node
        else:
            duplicate = self.head
            while duplicate.next:
                duplicate = duplicate.next
            duplicate.next = Nodel(data, None)
    def insert_values(self,data_list):  #takes a lists and creates a new linked-list
        self.head=None
        for data in data_list:
            self.insertatend(data)
    def getlength(self):
        itr=self.head
        c=0
        while itr:
            c+=1
            itr=itr.next
        print(f"The total number of elements in a given linked list= {c}")
        return c
    def removeatindex(self,index):
        if index < 0 or index >= (self.getlength()):
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next  #and python will clear the memory (memory occupied by delinked node)
        else :
            itr=self.head
            c=-1
            while itr:
                c+=1
                if(c==(index-1)):
                    itr.next=itr.next.next
                    break
                itr=itr.next
    def insertatindex(self,index,val):
        if index<0 or index>=self.getlength():
            raise Exception("Invalid Index Provided")
        if index==0:
            self.insertatbeg()
        else:
            itr=self.head
            c=0
            while itr:
                if c==(index-1):
                    node=Nodel(val,itr.next)
                    itr.next=node
                    break
                itr=itr.next
                c+=1







la = linkedlist()
la.insertatbeg(5)
la.insertatbeg(25)
la.print()
la.insertatend(29)
la.print()
la.insert_values(['Apple','Banana','Grapes','Guava','Orange'])
la.print()
la.getlength()
la.removeatindex(2)
la.insertatindex(2,'Pineapple')
la.print()