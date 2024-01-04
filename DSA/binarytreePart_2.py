class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    def findmin(self):
        if self.left is None:
            return self.data
        return self.left.findmin()
    def findmax(self):
        if self.right is None:
            return self.data
        return self.right.findmax()
    def deletenode(self,data):
        if data<self.data:
            if self.left:
                self.left=self.left.deletenode(data)
            else:
                return False
        elif data>self.data:
            if self.right:
                self.right=self.right.deletenode(data)
            else:
                return False
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            minvalue=self.right.findmin()
            self.data=minvalue
            self.right=self.right.deletenode(minvalue)
        return self

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.deletenode(20)
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())