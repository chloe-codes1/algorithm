T = int(input())

def bfs(Q, d):
    global result
    if end in Q:
        result.append(d)
        return
    for q in Q:
        if not visited[q]:
            visited[q] = 1
            if bfs(nodes[q], d+1):
                result.append(bfs(nodes[q],d+1))
            visited[q]=0

for t in range(1, T+1):
    V, E = map(int, input().split())
    nodes = dict()
    visited = [None] + [0]*V
    result = []
    for i in range(1, V+1):
        nodes[i] = []
    for _ in range(E):
        a,b = map(int,input().split())
        nodes[a].append(b)
        nodes[b].append(a)
    s, end = map(int, input().split())
    visited[s] = 1
    bfs(nodes[s],1)

    print(result)
    # print('#{} {}'.format(t, min(result) if result else 0))