

def DFS(graph):
    visited = [ False for _ in range(1, len(graph)+1) ]
    stack = [0]

    while stack:


        node = stack.pop()
        if visited[node] == False:
            visited[node] = True
            for n in graph[node+1]:
                if n not in stack:
                    stack.append(n)


    return stack



value, edge = map(int, input().split())

graph = {node+1: [] for node in range(value)}

for e in range(edge):
    f, t = map(int, input().split())
    graph[f].append(t) 


print(graph)


print(DFS(graph))

