class tree:
    def __init__ (self,name,designation):
        self.parents=None
        self.data=[name,designation]
        self.children=[]
    def add_child(self,child):
        self.children.append(child)
        child.parents=self
    def getlevel(self):
        level=0
        p=self.parents
        while p:
            level+=1
            p=p.parents
        return level
    def printtree(self,condition):
        spaces=" "*self.getlevel()
        if condition =="name":
            print(spaces+self.data[0])
        elif condition =="designation":
            print(spaces+self.data[1])
        else:
            part1=self.data[0]
            part2=self.data[1]
            print(spaces+part1+" "+part2)

        if len(self.children)>0:
            for i in self.children:
                i.printtree(condition)
root=tree("Nilupul","CEO")

primary=tree("Rahul","CTO")
secondary=tree("Vishva","Infrastructure Head")
third=tree("Dhawal","Cloud Manager")
third2=tree("Abhijeet","App Manager")
secondary2=tree("Aamir","Application Head")
primary1=tree("Gels","HR Head")
secondaryII=tree("Peter","Recruitment Manager")
secondaryIII=tree("Waqas","Policy Manager")

root.add_child(primary)
root.add_child(primary1)
primary.add_child(secondary)
primary.add_child(secondary2)
secondary.add_child(third)
secondary.add_child(third2)
primary1.add_child(secondaryII)
primary1.add_child(secondaryIII)

root.printtree("name")
root.printtree("designation")
root.printtree("both")
