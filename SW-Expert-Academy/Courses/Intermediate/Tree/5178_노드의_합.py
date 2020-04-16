T = int(input())
for t in range(1,T+1):
    N, M, L = map(int, input().split())
    nodes = [0]*(N+1)
    for _ in range(M):
        node, val = map(int, input().split())
        nodes[node] = val
    if len(nodes)%2:
        nodes.append(0)
    for i in range(len(nodes)-1, 1, -2):
        nodes[i//2] = nodes[i] + nodes[i-1]
    print('#{} {}'.format(t, nodes[L]))
