from queue import Queue
graph={
       'A':['B','C'],
       'B':['D','E'],
       'C':['F'],
       'D':[],
       'E':['F'],
       'F':[]
       }

visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m=queue.pop(0)
        print(m)
        
        for adj in graph[m]:
            if adj not in visited:
                visited.append(adj)
                queue.append(adj)
bfs(visited,graph,'A')