class graph:
    def __init__ (self,edges):
        self.edges=edges
        self.mydict={}
        for start,end in edges:
            if start in self.mydict:
                self.mydict[start].append(end)
            else:
                self.mydict[start]=[end]
        print(self.mydict)
    def getpaths(self,origin,destination,path=[]):
        path=path+[origin]

        if origin==destination:
            return[path]
        if origin not in self.mydict:
            return []
        path=[]
        for node in self.mydict[origin]:
            if node not in path:
                new_path=self.getpaths(node,destination,path)
                for p in new_path:
                    path.append(p)
        return path
    def get_shortestpath(self,origin,destination,path=[]):
        path=path+[origin]
        if origin not in self.mydict:
            return None
        if origin==destination:
            return path
        shortest_path=None
        for node in self.mydict[origin]:
            if node not in path:
                sp=self.get_shortestpath(node,destination,path)
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path=sp
        return shortest_path



                
if __name__ == "__main__":
    routes=[("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("Dubai","New York"),
        ("New York","Toronto")
    ]
route_graph=graph(routes)
origin="Mumbai"
destination="New York"
print(f"The Shortest Paths between {origin} and {destination}: ",route_graph.getpaths(origin,destination))
