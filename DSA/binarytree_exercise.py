class binary_tree:
    def __init__ (self,data):
        self.data=data
        self.left=None
        self.right=None
    def addchild(self,data):
        if data==self.data:
            return
        if data<self.data:
            if self.left:
                self.left.addchild(data)
            else:
                self.left=binary_tree(data)
        elif data>self.data:
            if self.right:
                self.right.addchild(data)
            else:
                self.right=binary_tree(data)
    def find_min(self):
        elem=None
        if self.left:
            elem=self.left.find_min()
        else:
            return self.data
        return elem
    def find_max(self):
        elem=None
        if self.right:
            elem=self.right.find_max()
        else:
            return (self.data)
        return elem
        
    def calculatesum(self):
        sum=0
        if self.left:
            sum+=self.left.calculatesum()
        sum+=self.data
        if self.right:
            self.right.calculatesum()
        return sum
    def preorder_traversal(self):
        element=[self.data]
        if self.left:
            element+=self.left.preorder_traversal()
        if self.right:
            element+=self.right.preorder_traversal()
        return element
    def postorder_traversal(self):
        element=[]
        if self.left:
            element+=self.left.postorder_traversal()
        if self.right:
            element+=self.right.postorder_traversal()
        element.append(self.data)
        return element
def built_tree(element):
    root=binary_tree(element[0])

    for i in range(1,len(element)):
        root.addchild(element[i])
    return root
if __name__== '__main__':
    element=[17, 4, 1, 20, 9, 23, 18, 34]
    save=built_tree(element)
    print(save.find_max())
    print(save.find_min())
    p=save.preorder_traversal()
    print(p)
    print(save.postorder_traversal())
    # print(save.find_max)
