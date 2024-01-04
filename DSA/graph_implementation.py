class graph:
    def __init__(self,nodes,is_directed=False):
        self.nodes=nodes
        self.adj_list={}
        self.is_directed=is_directed

        for node in self.nodes:
            self.adj_list[node]=[]
    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        if not self.is_directed:
            self.adj_list[v].append(u)
    def degreeof(self,node):
        deg=len(self.adj_list[node])
        return deg
    def print_adjacency(self):
        for node in self.nodes:
            print(node,":",self.adj_list[node])
nodes=["A","B","C","D","E"]
all_edges=[("A","B"),("A",'C'),("B","D"),("C","D"),("C","E"),("D","E")]
grap=graph(nodes,True)
for u,v in all_edges:
    grap.add_edge(u,v)
grap.print_adjacency()
degree=grap.degreeof("C")
print("The degree of C is: ",degree)
    