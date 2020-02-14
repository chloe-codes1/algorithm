import sys
sys.stdin = open('input.txt')


def DFS(v):
    stack = []
    stack.append(v)
    visited[v] = 1
    print(v, end='-')

    while stack:
        p = v
        for i in G[v]:
            if not visited[i]: #방문 안했으면
                stack.append(i)
                v = i
                visited[i] = 1
                print(v, end='-')
                break
        
        else:
            if p==v:
                v = stack.pop()



V, E = map(int, input().split())


G = [[] for _ in range(V+1)] # index가 아닌 정수값 그대로를 쓰기 위해 +1함

visited = [0 for _ in range(V+1)]

for i in range(E):
    u, v = map(int, input().split())

    G[u].append(v)
    G[v].append(u)


DFS(1)