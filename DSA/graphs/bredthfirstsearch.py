#Breadth first Search
from queue import Queue 
adj_list={
    "A" : ['B', 'D'],
    "B" : ['A','C'],
    "C" : ['B'],
    "D" : ['A','E','F'],
    "E" : ['D','F','G'],
    "F": ['D', 'E','H'],
    "G": ['H', 'E'],
    "H": ['G', 'F']
}
visited={}
level={} #Distance Dictionary
parent={}
bfs_traversal_output=[]
queue=Queue()
for node in (adj_list.keys()):
    visited[node]=False
    parent[node]=None
    level[node]=-1
print(visited)
print(level)
print(parent)

s="A"
visited[s]=""
level[s]=0
queue.put(s)

while not queue.empty():
    u=queue.get()
    bfs_traversal_output.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            level[v]=level[u]+1
            queue.put(v)
print(bfs_traversal_output)