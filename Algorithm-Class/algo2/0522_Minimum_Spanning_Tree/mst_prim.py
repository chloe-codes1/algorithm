# Prim Algorithm
# : 하나의 정점에서 연결된 간선들 중에 하나씩 선택 하면서 MST를 만들어 가는 방식

# 우선순위 큐 활용하기 -> 이진힙 -> heapq
import heapq

"""
MST  + 인접행렬

7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51

시작정점 끝정점 가중치

결과
[0, 21, 31, 34, 46, 18, 25]
175
"""

V, E = map(int, input().split())
adj = {i: [] for i in range(V)}
for i in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e,c])
    adj[e].append([s,c]) #무방향이라서
# print(adj)

# key, mst, 우선순위 큐 준비
INF = float('inf')
key = [INF] * V
mst = [False] * V
pq = []
# 시작 정점 선택 : 0
key[0] = 0
# 큐에 시작 정점을 넣음 => (key, 정점 index) 묶어서 넣기
# 우선순위 큐 => 이진힙 => heapq 라이브러리 사용
heapq.heappush(pq, (0,0)) # heqppush(배열 정보, 어떤 원소 넣을 지) : heap의 구조를 유지하면서 하나의 원소를 넣어줌
                    # 우선순위큐 -> 원소의 첫번째 요소 -> key를 우선순위로
result = 0
while pq:
    # 최소값 찾기
    k, node = heapq.heappop(pq) #내가 갖고있는 heapq에서 최소값을 pop해줌
    if mst[node]: continue # 갱신 할 때 필요했던 정보는 skip하기
    # mst로 선택
    mst[node] = True
    result += k
    # key값 갱신 => key배열 / 큐
    for destination, weight in adj[node]:
        if not mst[destination] and key[destination] > weight:
            key[destination] = weight
            # 큐 갱신 => 새로운 (key, 정점) 삽입 => 필요없는 원소는 skip
            heapq.heappush(pq, (key[destination], destination))

print(result)