class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_children(self,child):
        child.parent=self
        self.children.append(child)
    def getlevel(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_tree(self):
        space='  '*self.getlevel()
        print(space+self.data)
        if len(self.children)>0:
            for child in self.children:
                child.print_tree()
def built_product_tree():
    root=TreeNode("Electronics")
    laptop=TreeNode("Laptop")
    root.add_children(laptop)
    laptop.add_children(TreeNode("Mac"))
    surface=TreeNode("Surface")
    laptop.add_children(surface)
    laptop.add_children(TreeNode("Thinkpad"))

    mobile=TreeNode("Mobile")
    root.add_children(mobile)
    mobile.add_children(TreeNode("iphone"))
    mobile.add_children(TreeNode("Vivo"))
    mobile.add_children(TreeNode("Google Pixel"))

    television=TreeNode("Televison")
    root.add_children(television)
    television.add_children(TreeNode("Samsung"))
    television.add_children(TreeNode("Onida"))
    television.add_children(TreeNode("Sony"))
    return root

if __name__ == '__main__':
    root=built_product_tree()
    root.print_tree()
    pass