from queue import Queue

adj_list={
    "A":["B","D"],
    "B":["A","C"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "H":["G","F"]
}
#bfs code

visited={}
level={}#distance
parent={}
bfs_traversal_output=[]
queue=Queue()


for node in adj_list.keys():
    visited[node]=False
    parent[node]=None
    level[node]=-1 #infyinity 
# print(visited)
# print(parent)
# print(level)
s="A"
visited[s]=True
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
print(visited)
print(level)
print("D",level["D"])
path=[]
v="G"
while v is not None:
    path.append(v)
    v=parent[v]
path.reverse()
print(path)
    
    