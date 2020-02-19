import sys

sys.stdin = open('input.txt')



def DFS(v):
    stack = []
    visited[v] = 1

    stack.append(v)

    print(str(v) , end= ' ')

    while stack:
        temp = v
        for spot in graph[v]:
            if not visited[spot]:
                stack.append(spot)
                visited[spot] =  1
                v = spot
                print(str(v) , end = ' ')
                break
        else:
            if temp == v:
                v = stack.pop()

vertex, edge = map(int, input().split())

graph = [ [] for _ in range(vertex +1)]
visited = [ 0 for _ in range(vertex +1)]

for i in range(edge):
    f, t = map(int, input().split())

    graph[f].append(t)
    graph[t].append(f)

DFS(1)