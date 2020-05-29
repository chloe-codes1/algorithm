# import heapq

# T = int(input())

# for t in range(1, T+1):

#     V, E = map(int, input().split())
#     V+=1
#     adj = {i: [] for i in range(V)}
#     for i in range(E):
#         s, e, c = map(int, input().split())
#         adj[s].append([e,c])
#         adj[e].append([s,c]) 

#     INF = float('inf')
#     key = [INF] * V
#     mst = [False] * V
#     pq = []
#     key[0] = 0
#     heapq.heappush(pq, (0,0)) 
#     result = -1
#     while pq:
#         k, node = heapq.heappop(pq) 
#         # if mst[node]: continue 
#         mst[node] = True
#         # result += k
#         if node == V:
#             result = key[node]
#             break
#         for destination, weight in adj[node]:
#             if not mst[destination] and key[destination] > weight:
#                 key[destination] = weight
#                 heapq.heappush(pq, (key[destination], destination))
#     print(result)



import heapq

T = int(input())

for t in range(1, T+1):

    V, E = map(int, input().split())
    V+=1
    adj = {i: [] for i in range(V)}
    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e,c])

    INF = float('inf')
    key = [INF] * V
    pq = []
    key[0] = 0
    heapq.heappush(pq, (0,0)) 
    result = -1
    while pq:
        k, node = heapq.heappop(pq) 
        if node == V-1:
            result = key[node]
            break
        for destination, weight in adj[node]:
            if key[weight] > destination +k:
                key[weight] = destination +k
                heapq.heappush(pq, (key[destination], destination+ k))
    print(result)