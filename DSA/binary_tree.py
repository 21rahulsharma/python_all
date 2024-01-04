class binary_tree:
    def __init___ (self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data==self.data:
            return 
        if data <self.data:
            #add data in left sub-tree
            if self.left:
                self.left.add_child(data)
                pass
            else:
                self.left=binary_tree(data)
        else:
            #add data in right sub tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right=binary_tree(data)
    def inorder_traversal(self):
        elements=[]
        #Visiting the left tree first 
        if self.left:
            elements +=self.left.inorder_traversal()

        #Visiting the root node 
        elements.append(self.data)

        #Visiting the right node 
        if self.right:
            elements +=self.right.inorder_traversal()     
        return elements  
def build_tree(elements):
    root=binary_tree(elements[0])         
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
        
if __name__=='__main__':
    numbers =[17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.inorder_traversal())

